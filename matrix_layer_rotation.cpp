#include <bits/stdc++.h>
#include <iostream>>
using namespace std;

string ltrim(const string &);
string rtrim(const string &);
vector<string> split(const string &);

void printaMatriz(vector<vector<int>> matrix){
    for(int i = 0; i < matrix.size(); i++){
        for(int j = 0; j < matrix[0].size(); j++){
            cout << matrix[i][j] << " ";
        }
        cout << "\n";
    }
    cout << "\n";
    cout << "\n";
}

// vector<vector<int>> rodar(vector<vector<int>> matrix){
    

//     return matrix;
// }

// Complete the matrixRotation function below.
void matrixRotation(vector<vector<int>> matrix, int r) {
    if(r == 0){
        return;
    }
    int linhas = matrix.size();
    int colunas = matrix[0].size();
    int numberOfCicles = (min(colunas,linhas)/2);
    for(int k = 0; k < numberOfCicles; k++){
        int module = (2 * (matrix.size() - (2 * k))) + (2 * (matrix[0].size() - (2 * k))) - 4;
        int limiteRotations = r%module;
        
        for(int p = 0; p < limiteRotations; p++){

            int firstLine = 0 + k;
            int lastLine = linhas - k - 1;
            int firstColumn = 0 + k;
            int lastColumn = colunas - k - 1;

            int x = matrix[firstLine][lastColumn];
            int aux = 0;
            for(int i = lastColumn; i > firstColumn; i--){
                aux = matrix[firstLine][i-1];
                matrix[firstLine][i-1] = x;
                x = aux;
            }

            for(int i = firstLine; i < lastLine; i++){
                aux = matrix[i+1][firstColumn];
                matrix[i+1][firstColumn] = x;
                x = aux;
            }

            for(int i = firstColumn; i < lastColumn; i++){
                aux = matrix[lastLine][i+1];
                matrix[lastLine][i+1] = x;
                x = aux;
            }

            for(int i = lastLine; i > firstLine; i--){
                aux = matrix[i - 1][lastColumn];
                matrix[i - 1][lastColumn] = x;
                x = aux;
            }
        }
    }  
    printaMatriz(matrix);
    return;
    

}



int main()
{
    string mnr_temp;
    getline(cin, mnr_temp);

    vector<string> mnr = split(rtrim(mnr_temp));

    int m = stoi(mnr[0]);

    int n = stoi(mnr[1]);

    int r = stoi(mnr[2]);

    vector<vector<int>> matrix(m);

    for (int i = 0; i < m; i++) {
        matrix[i].resize(n);

        string matrix_row_temp_temp;
        getline(cin, matrix_row_temp_temp);

        vector<string> matrix_row_temp = split(rtrim(matrix_row_temp_temp));

        for (int j = 0; j < n; j++) {
            int matrix_row_item = stoi(matrix_row_temp[j]);

            matrix[i][j] = matrix_row_item;
        }
    }

    matrixRotation(matrix, r);

    return 0;
}

string ltrim(const string &str) {
    string s(str);

    s.erase(
        s.begin(),
        find_if(s.begin(), s.end(), not1(ptr_fun<int, int>(isspace)))
    );

    return s;
}

string rtrim(const string &str) {
    string s(str);

    s.erase(
        find_if(s.rbegin(), s.rend(), not1(ptr_fun<int, int>(isspace))).base(),
        s.end()
    );

    return s;
}

vector<string> split(const string &str) {
    vector<string> tokens;

    string::size_type start = 0;
    string::size_type end = 0;

    while ((end = str.find(" ", start)) != string::npos) {
        tokens.push_back(str.substr(start, end - start));

        start = end + 1;
    }

    tokens.push_back(str.substr(start));

    return tokens;
}


