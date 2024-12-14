using System;

class Program
{
    static void Main()
    {
        // Questions and answers
        string[] questions = {
            "What is 9! ?",
            "What is 21 * 3 ?",
            "What is 76 * 4 ?",
            "What is 7.6 * 6.0 ?",
            "What is 3! ?",
            "What is 4! ?",
            "What is (3! / 2!) + (cube root of 729 + 3 * (10 - 3) / 2 + 1) ?"
        };

        double[] answers = {
            Factorial(9),
            21 * 3,
            76 * 4,
            7.6 * 6.0,
            Factorial(3),
            Factorial(4),
            (Factorial(3) / Factorial(2)) + (Math.Cbrt(729) + 3 * (10 - 3) / 2 + 1)
        };

        // Display questions and answers
        for (int i = 0; i < questions.Length; i++)
        {
            Console.WriteLine(questions[i]);
            Console.WriteLine("Answer: " + answers[i]);
            Console.WriteLine();
        }
    }

    // Factorial function
    static double Factorial(int n)
    {
        if (n <= 1) return 1;
        return n * Factorial(n - 1);
    }
}
