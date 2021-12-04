// See https://aka.ms/new-console-template for more information

Console.WriteLine("Day 2 - Task 2");

var horizontal = 0;
var depth = 0;
var aim = 0;

foreach (string line in File.ReadLines(@"input.txt"))
{
    var lineParts = line.Split(' ');
    var numver = int.Parse(lineParts[1]);

    switch (lineParts[0])
    {
        case "forward":
            horizontal += numver;
            depth += numver * aim;
            break;
        case "up":
            aim -= numver;
            break;
        case "down":
            aim += numver;
            break;
    }


}

Console.WriteLine("Postition: {0}", horizontal);
Console.WriteLine("Aim: {0}", aim);
Console.WriteLine("depth: {0}", depth);
try
{
    Console.WriteLine("Product: {0}", horizontal * depth);
}
catch (OverflowException e)
{
    Console.WriteLine(e.ToString());
}
