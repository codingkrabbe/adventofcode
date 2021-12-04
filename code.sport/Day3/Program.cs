// See https://aka.ms/new-console-template for more information
using System.Text;

Console.WriteLine("Day 3 - Task 1");

var values = File.ReadLines(@"input.txt").ToArray();
var digits = values[0].Length;

var rate = new int[digits];

foreach (var value in values)
{
    var valueDigits = value.ToCharArray();

    for (var i = 0; i < digits; i++)
    {
        if (valueDigits[i] == '1')
        {
            rate[i]++;
        }
    }
}

var gammaRateString = new StringBuilder();

foreach (var rateItem in rate)
{
    if (rateItem > (values.Length / 2))
    {
        gammaRateString.Append('1');
    }
    else
    {
        gammaRateString.Append('0');
    }
}

var gammaRate = Convert.ToInt32(gammaRateString.ToString(), 2);
var mask = Convert.ToInt32(Math.Pow(2, digits) - 1);
var epsilonRate = (~gammaRate) & mask;

Console.WriteLine("gammaRate:\t{0}", gammaRateString.ToString());
Console.WriteLine("epsilonRate:\t{0}", Convert.ToString(epsilonRate, 2));
Console.WriteLine("result:\t{0}", gammaRate * epsilonRate);
