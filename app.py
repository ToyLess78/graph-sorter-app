import os
import time
import psutil
from flask import Flask, request, render_template, redirect, url_for, send_file
from werkzeug.utils import secure_filename
from collections import defaultdict, deque

# Flask Configuration
app = Flask(__name__)
UPLOAD_FOLDER = './uploads'
RESULT_FOLDER = './results'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['RESULT_FOLDER'] = RESULT_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
if not os.path.exists(RESULT_FOLDER):
    os.makedirs(RESULT_FOLDER)

# File validation and logic functions
def validate_file(file_path):
    if not file_path.endswith('.txt'):
        raise ValueError("Invalid file format. The file must be a .txt file.")
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"The file '{file_path}' does not exist.")
    with open(file_path, 'r') as file:
        lines = file.read().splitlines()
    for line in lines:
        if not line.isdigit() or len(line) != 6:
            raise ValueError(f"Invalid line in file: '{line}'. Each line must be a 6-digit number.")
    return lines


def build_graph(pieces):
    graph = defaultdict(list)
    for i, piece1 in enumerate(pieces):
        for j, piece2 in enumerate(pieces):
            if i != j and piece1[-2:] == piece2[:2]:
                graph[piece1].append(piece2)
    return graph


def find_longest_path(graph, start_piece):
    queue = deque([(start_piece, [start_piece])])
    longest_path = []

    while queue:
        current, path = queue.popleft()
        if len(path) > len(longest_path):
            longest_path = path
        for neighbor in sorted(graph[current], key=lambda x: (len(graph[x]), x), reverse=True):
            if neighbor not in path and current[-2:] == neighbor[:2]:
                queue.append((neighbor, path + [neighbor]))
    return longest_path


def improve_with_remaining(pieces, main_sequence):
    used = set(main_sequence)
    remaining = sorted(set(pieces) - used)
    for piece in list(remaining):
        if main_sequence[-1][-2:] == piece[:2]:
            main_sequence.append(piece)
            remaining.remove(piece)
        elif main_sequence[0][:2] == piece[-2:]:
            main_sequence.insert(0, piece)
            remaining.remove(piece)
    return main_sequence


def validate_sequence(sequence):
    for i in range(len(sequence) - 1):
        if sequence[i][-2:] != sequence[i + 1][:2]:
            return False, i
    return True, -1


def merge_sequence(sequence):
    if not sequence:
        return ""
    merged = sequence[0]
    for i in range(1, len(sequence)):
        merged += sequence[i][2:]
    return merged


def save_sequence_to_file(sequence, output_file_path):
    with open(output_file_path, 'w') as file:
        for item in sequence:
            file.write(f"{item}\n")
    return output_file_path


# Routes
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return "No file part"
        file = request.files['file']
        if file.filename == '':
            return "No selected file"
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        # Run the sorting logic
        try:
            start_time = time.time()
            process = psutil.Process(os.getpid())
            cpu_before = process.cpu_times()
            memory_before = process.memory_info().rss / (1024 ** 2)

            numbers = validate_file(file_path)
            graph = build_graph(numbers)
            start_piece = min((piece for piece, connections in graph.items() if len(connections) == 1), default=numbers[0])
            longest_path = find_longest_path(graph, start_piece)
            final_sequence = improve_with_remaining(numbers, longest_path)
            is_valid, error_index = validate_sequence(final_sequence)
            merged_sequence = merge_sequence(final_sequence)

            cpu_after = process.cpu_times()
            memory_after = process.memory_info().rss / (1024 ** 2)
            end_time = time.time()

            user_cpu_time = cpu_after.user - cpu_before.user
            system_cpu_time = cpu_after.system - cpu_before.system
            total_cpu_time = user_cpu_time + system_cpu_time

            # Save the result
            result_file = save_sequence_to_file(final_sequence, os.path.join(app.config['RESULT_FOLDER'], 'sortedlist.txt'))

            # Render results
            return render_template(
                'result.html',
                total_pieces=len(final_sequence),
                is_valid=is_valid,
                merged_sequence=merged_sequence,
                execution_time=round(end_time - start_time, 2),
                cpu_time=round(total_cpu_time, 2),
                memory_used=round(memory_after - memory_before, 2),
                result_file=result_file
            )

        except Exception as e:
            return str(e)

    return render_template('index.html')


@app.route('/download/<path:filename>', methods=['GET'])
def download_file(filename):
    return send_file(filename, as_attachment=True)


# Templates
@app.route('/template')
def template():
    return "This would be used for your HTML templates"


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
