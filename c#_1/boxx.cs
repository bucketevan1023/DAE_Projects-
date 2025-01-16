using UnityEngine;

public class boxx : MonoBehaviour
{
    // Start is called once before the first execution of Update after the MonoBehaviour is created
    int number = 5;
    string king = "hello world";
 
    // Update is called once per frame
    void Start()
    {
        Debug.Log("hello world");    
        if (number>134){
            Debug.Log("the numberis bigger then 134");

        }
        else{
            Debug.Log("the number is smaller then 134");
        }
        for (int i = 1; i <= 5; i++){
            Debug.Log("Number: " + i);

        }
        
           
        
    }
    
    
        
    
}