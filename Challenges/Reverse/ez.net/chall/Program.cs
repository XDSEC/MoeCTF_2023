Console.WriteLine("Give me your flag!");
var flag = Console.ReadLine();
Console.WriteLine("You gave me: {0}", flag);
if (flag == KoitoCoco.MoeCtf.FlagHelper.Flag)
{
    Console.WriteLine("You got it!");
    Console.WriteLine("But something went wrong!!!");
}
else
{
    Console.WriteLine("Nope!");
    System.Environment.Exit(0);
}
while (true) {
    var a = Random.Shared.Next(0, 1000);
    var b = Random.Shared.Next(0, 10);
    Console.WriteLine("Welcome to Cirno's Math Classroom! Let's practice! {0} / {1} = {2}", a, b, a/b);
}