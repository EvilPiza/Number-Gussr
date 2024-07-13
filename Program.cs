using System;

namespace DerrySucks
{
    class Program
    {
        static void Main(string[] args)
        {
            Random random = new Random();

            int numbr = random.Next(1, 50); // THE TYPO IS ON PURPOSE DERRY

            int lives = 5;

            while (lives != 0)
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
                        Console.WriteLine("No way you won!!");
                    }
                }
                catch (FormatException)
                {
                    Console.WriteLine($"Your input was not a number.");
                }


            }
        }
    }
}
