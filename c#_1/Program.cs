using System;
using System.Collections.Generic;

class SecretBoxingMatch // Class demonstrating access levels
{
    // Private field (can only be accessed within this class)
    private string matchDetails = "Top secret boxing match";

    // Public method (can be accessed outside this class)
    public void ShowMatchDetails()
    {
        Console.WriteLine("Accessing Private Data: " + matchDetails);
    }
}

class Program
{
    static void Main()
    {
        Console.WriteLine("Hello, World!");

        // Demonstrating Variables with Data Types
        int myVariable = 12;
        bool isGameActive = false;
        double myDouble = 3.15;

        //  Demonstrating List (Array)
        List<string> enemies = new List<string>();
        enemies.Add("Witch");
        enemies.Add("Swordsman");
        enemies.Add("Goblin");

        // Loop through the list
        Console.WriteLine("Enemy List:");
        foreach (string enemy in enemies)
        {
            Console.WriteLine("- " + enemy);
        }

        // Calling a Function
        int sum = Add(6, 4);
        Console.WriteLine("Sum: " + sum);

        // Demonstrating Access Levels
        SecretBoxingMatch match = new SecretBoxingMatch();
        match.ShowMatchDetails(); // Accessing private data through a public method
    }

    //  Function Example
    static int Add(int a, int b)
    {
        return a + b;
    }
}
