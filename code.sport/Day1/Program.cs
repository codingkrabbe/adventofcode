// See https://aka.ms/new-console-template for more information
Console.WriteLine("Day 1 - Task 1");

int? previousMeasurement = null;
var increased = 0;
var decreased = 0;

foreach (string line in File.ReadLines(@"input.txt"))
{
    var number = int.Parse(line);
    if (previousMeasurement != null)
    {
        if (previousMeasurement < number)
        {
            increased++;
        }
        else if (previousMeasurement > number)
        {
            decreased++;
        }
    }
    previousMeasurement = number;

}

Console.WriteLine("increased:\t{0}", increased);
Console.WriteLine("decreased:\t{0}", decreased);

Console.WriteLine("-----------------------------------------------------------------");

Console.WriteLine("Day 1 - Task 2");

previousMeasurement = null;
increased = 0;
decreased = 0;
var values = File.ReadLines(@"input.txt").Select(int.Parse).ToArray();

for (var i = 0; i < values.Length - 2; i++)
{
    if (i + 2 >= values.Length)
    {
        Console.Error.WriteLine("Not in array!");
    }
    var sum = values[i] + values[i + 1] + values[i + 2];
    if (previousMeasurement < sum)
    {
        increased++;
    }
    else if (previousMeasurement > sum)
    {
        decreased++;
    }
    previousMeasurement = sum;
}

Console.WriteLine("increased:\t{0}", increased);
Console.WriteLine("decreased:\t{0}", decreased);