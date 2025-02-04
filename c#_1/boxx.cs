using UnityEngine;

public class Boxx : MonoBehaviour
{
    //  Variables with different data types
    private int number = 5; // Example of a private field
    public string king = "Hello World"; // Example of a public field

    // Start() is called once before the first frame update
    void Start()
    {
        Debug.Log("Hello, World");

        //  Conditional Statement
        if (number > 134)
        {
            Debug.Log("The number is bigger than 134");
        }
        else
        {
            Debug.Log("The number is smaller than 134");
        }

        //  Loop Example
        for (int i = 1; i <= 5; i++)
        {
            Debug.Log("Number: " + i);
        }
    }
}
