#  🧩 Graph Sorter App 

[Live Demo 🚀](https://graph-sorter.up.railway.app/)

Graph Sorter App is a minimalist Flask-based application designed to process files containing sequences of 6-digit numbers. It validates the sequences and sorts them using a graph-based algorithm, ensuring the sequences are merged optimally.

---

## ✨ Features

- **Validation**: Ensures the uploaded file is properly formatted with 6-digit numbers (one per line).
- **Sorting Logic**: Implements graph construction and pathfinding to optimize the sequence.
- **Performance Metrics**: Displays execution time, CPU usage, and memory consumption.
- **Downloadable Results**: Provides the processed file for download.
- **Real-Time Error Handling**: Displays validation errors on the page without reloading.

---

## 🛠 Sorting Methods

1. **Graph Construction**:
   - Treats each sequence as a graph node.
   - Establishes directed edges between nodes where the last two digits of one node match the first two of another.

2. **Longest Path Finding**:
   - Uses Breadth-First Search (BFS) to identify the longest path starting from a minimally connected node.

3. **Remaining Piece Integration**:
   - Incorporates unused nodes into the sequence, ensuring completeness.

4. **Sequence Validation**:
   - Verifies that all adjacent nodes in the sequence maintain correct relationships.

5. **Sequence Merging**:
   - Combines the sorted sequences into a single cohesive string.

---

## 🔧 Prerequisites

- **Python 3.7 or higher**
- Required dependencies:
  ```bash
  pip install flask werkzeug psutil

- - -

## 🏃‍ How to Run

1.  **Clone the Repository**:
    
   ```bash
    git clone https://github.com/ToyLess78/graph-sorter-app.git
    cd graph-sorter-app
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
    
    *   Open your browser and navigate to
```bash
    http://127.0.0.1:5000
 ```
- - -

## 📋 Usage Instructions

1.  **Upload a File**:
    
- The uploaded file should be a `.txt` file containing 6-digit numbers, one per line.
2.  **View Results**:
    
- The app displays metrics like the total number of pieces, execution time, and resource usage.
3.  **Download Sorted File**:
    
- Click on the provided link to download the processed file.
4.  **Error Handling**:
    
- If the file contains invalid lines or format issues, an error message is displayed without reloading the page.

- - -

## 📁 File Structure

*   **`app.py`**: Main application logic.
*   **`templates/`**: Contains HTML templates for the upload page and results page.
*   **`static/`**: Holds static assets like CSS, JavaScript, and images.
*   **`uploads/`**: Directory for uploaded files.
*   **`results/`**: Directory for storing processed files.

- - -

## ⚠️ Known Limitations

*   The application currently supports only `.txt` files with valid numeric sequences.
*   The sorting logic assumes input sequences are well-formed and non-overlapping.

- - -

## 📊 Example Input and Output

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

## 🤝 Contribution

Feel free to fork the repository and submit pull requests for any improvements or additional features.

## 🎉 Happy Sorting!

```bash
This README provides a concise overview of your application while maintaining clarity and usability for potential users.
```