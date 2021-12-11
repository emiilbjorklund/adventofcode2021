#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <algorithm>
#include <regex>

using namespace std;

void print(vector<vector<int>> &grid)
{
    int danger = 0;

    for (int i = 0; i < grid.size(); i++)
    {
        for (int j = 0; j < grid[i].size(); j++)
        {
            if (grid[i][j] >= 2)
            {
                danger++;
            }
        }
    }

    cout << danger;
}

void explode(int x1, int y1, int x2, int y2, vector<vector<int>> &grid)
{

    if (grid.size() < max(y1, y2))
    {
        grid.resize(max(y1, y2) + 1);
    }

    for (int i = min(y1, y2); i <= max(y1, y2); i++)
    {
        if (grid[i].size() < max(x1, x2))
        {
            grid[i].resize(max(x1, x2) + 1);
        }
    }

    // vertical
    if (y1 == y2)
    {
        for (int i = min(x1, x2); i <= max(x1, x2); i++)
        {
            grid[y1][i] += 1;
        }
    }
    // horizontal
    else if (x1 == x2)
    {
        for (int i = min(y1, y2); i <= max(y1, y2); i++)
        {
            grid[i][x1] += 1;
        }
    }

    //diagonal
    else if (x1 != x2 && y1 != y2)
    {

        for (int i = min(y1, y2); i <= max(y1, y2); i++)
        {
            for (int j = min(x1, x2); j <= max(x1, x2); j++)
            {

                // Cross product
                int dxc = j - x1;
                int dyc = i - y1;

                int dxl = x2 - x1;
                int dyl = y2 - y1;

                if ((dxc * dyl - dyc * dxl) == 0)
                {
                    grid[i][j] += 1;
                }
            }
        }
    }
}

int main()
{

    vector<vector<int>> grid;
    vector<string> input;

    ifstream file("input.txt");
    string line, str;

    while (std::getline(file, line, ' '))
    {
        if (line != "->")
        {
            stringstream ss(line);
            while (getline(ss, str, '\n'))
            {
                input.push_back(str);
            }
        }
    }

    for (int i = 0; i < input.size() - 1; i += 2)
    {

        int x1 = stoi(input.at(i).substr(0, input.at(i).find(',')));
        int y1 = stoi(input.at(i).substr(input.at(i).find(',') + 1, input.at(i).size() - 1));

        int x2 = stoi(input.at(i + 1).substr(0, input.at(i + 1).find(',')));
        int y2 = stoi(input.at(i + 1).substr(input.at(i + 1).find(',') + 1, input.at(i + 1).size() - 1));

        explode(x1, y1, x2, y2, grid);
    }

    print(grid);
}