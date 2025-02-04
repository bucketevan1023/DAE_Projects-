using UnityEngine;

public class Boxx : MonoBehaviour
{
    // Variables with different data types
    int number = 5;
    string king = "Hello World";

    // Start() is called before the first frame update
    void Start()
    {
        Debug.Log("Hello, World");

        // Conditional Statement
        if (number > 134)
        {
            Debug.Log("The number is bigger than 134");
        }
        else
        {
            Debug.Log("The number is smaller than 134");
        }

        // Loop Example
        for (int i = 1; i <= 5; i++)
        {
            Debug.Log("Number: " + i);
        }
    }
}