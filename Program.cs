using Hors;
using System;

var hors = new HorsTextParser();
string text_raw = $"31 декабря {DateTime.Now.ToString("yyyy")} год";
var result = hors.Parse(text_raw, DateTime.Now);

var text = result.Text; 
var formatText = result.TextWithTokens; 
var date = result.Dates[0].DateFrom; 
System.Console.WriteLine(date);
System.Console.WriteLine(DateTime.Now);