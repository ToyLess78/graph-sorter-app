## README.md

### Graph Sorter App

Graph Sorter App is a lightweight Flask-based application that allows users to upload files containing sequences of 6-digit numbers, validates the sequences, and sorts them based on predefined rules. The app ensures that sequences are arranged optimally, combining related pieces into a cohesive final sequence.

- - -

### Features

*   **Validation**: Ensures uploaded files are in the correct format (6-digit numbers, one per line).
*   **Sorting**: Utilizes graph-based sorting algorithms to optimize sequences.
*   **Performance Metrics**: Displays execution time, CPU usage, and memory usage.
*   **Download Option**: Provides the sorted file for download.
*   **Responsive Feedback**: Displays error messages in case of validation issues.

- - -

### Sorting Methods

1.  **Graph Construction**:
    
    *   Each sequence is treated as a node in a graph.
    *   Directed edges are established where the last two digits of one sequence match the first two digits of another.
2.  **Finding Longest Path**:
    
    *   A breadth-first search (BFS) algorithm is used to find the longest path in the graph, starting from a sequence with minimal connections.
3.  **Improvement with Remaining Pieces**:
    
    *   Adds unused pieces to the sequence, ensuring all nodes are included.
4.  **Sequence Validation**:
    
    *   Checks whether the generated sequence maintains the relationship between adjacent nodes.
5.  **Merging**:
    
    *   Combines the sorted sequences into a single string.

- - -

### Prerequisites

*   **Python 3.7 or higher** installed.
*   Flask and required dependencies:
    
   ```bash
    pip install flask werkzeug psutil
   ```
    

- - -

### How to Run

1.  **Clone the Repository**:
    
   ```bash
    git clone https://github.com/ToyLess78/graph-sorter-app.git cd graph-sorter-app
  ```
    
2.  **Set Up Environment**:
    
    *   Create the necessary directories:
        
   ```bash
    mkdir uploads results
  ```

        
3.  **Run the Application**:
    
   ```bash
    python app.py
  ```
    
4.  **Access the App**:
    
    *   Open your browser and navigate to `http://127.0.0.1:5000`.

- - -

### Usage

1.  **Upload a File**:
    
    *   The uploaded file should be a `.txt` file containing 6-digit numbers, one per line.
2.  **View Results**:
    
    *   The app displays metrics like the total number of pieces, execution time, and resource usage.
3.  **Download Sorted File**:
    
    *   Click on the provided link to download the processed file.
4.  **Error Handling**:
    
    *   If the file contains invalid lines or format issues, an error message is displayed without reloading the page.

- - -

### File Structure

*   **`app.py`**: Main application logic.
*   **`templates/`**: Contains HTML templates for the upload page and results page.
*   **`static/`**: Holds static assets like CSS, JavaScript, and images.
*   **`uploads/`**: Directory for uploaded files.
*   **`results/`**: Directory for storing processed files.

- - -

### Known Issues

*   The application currently supports only `.txt` files with valid numeric sequences.
*   The sorting logic assumes input sequences are well-formed and non-overlapping.

- - -

### Example Input/Output

#### Input

   ```bash
   123456
   345678
   567890
```

#### Output

*   **Merged Sequence**: 
   ```bash
1234567890
```
*   **Metrics**:
    *   Execution Time: ~0.01 seconds
    *   CPU Time: ~0.002 seconds
    *   Memory Used: ~0.08 MB

- - -

### Contribution

Feel free to fork the repository and submit pull requests for any improvements or additional features.