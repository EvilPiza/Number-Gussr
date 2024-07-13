using System;
using System.Security.Cryptography.X509Certificates;

namespace DerrySucks
{
    class Program
    {
        static void Main(string[] args)
        {
            Random random = new();

            int numbr = random.Next(1, 50); // THE TYPO IS ON PURPOSE DERRY

            int lives = 5;

            while (lives > 0)
            {
                Console.WriteLine("What's your guess?");

                string? string_user_input = Console.ReadLine();

                try
                {
                    int.TryParse(string_user_input, out int user_input);                
                    if (user_input != numbr)
                    {
                        if (user_input > numbr)
                        {
                            Console.WriteLine("Try another number, lower maybe.");
                            lives--;
                        }
                        else if (user_input < numbr)
                        {
                            Console.WriteLine("Try another number, higher maybe.");
                            lives--;
                        }
                    }
                    else if (user_input == numbr)
                    {
                        lives = -1; // So nothing gets printed (very simple fix)
                        Win(numbr);
                    }
                }
                catch (FormatException)
                {
                    Console.WriteLine($"Your input was not a number."); // this doesn't work for some reason. if you know derry lmk.
                }
            }
            if (lives == 0)
            {
                Console.WriteLine("Awww! You ran out of lives!");
                Thread.Sleep(1000);
                Console.WriteLine($"The number was: {numbr}!");
            }
        }
        static void Win(int numbr)
        {
            Console.WriteLine("No way you won!");
            Thread.Sleep(1000);
            Console.WriteLine($"The number was: {numbr}!");
        }
    }
}
