using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        Console.WriteLine("Hello, World!");

        // Variables with different data types
        int myVariable = 12;
        bool isGameActive = false;
        double myDouble = 3.15;
        
        // Access Level Example (private variable inside a class)
        string secretBoxingMatch = "Top secret boxing match";

        // Array/List Example
        List<string> enemies = new List<string>();
        enemies.Add("Witch");
        enemies.Add("Swordsman");
        enemies.Add("Goblin");

        // Loop through the list
        foreach (string enemy in enemies)
        {
            Console.WriteLine("Enemy: " + enemy);
        }

        // Calling the function
        int sum = Add(6, 4);
        Console.WriteLine("Sum: " + sum);
    }

    // Function Example
    static int Add(int a, int b)
    {
        return a + b;
    }
}