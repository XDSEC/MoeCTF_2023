using System.Reflection;
using System.Text;

var assembly = Assembly.LoadFile("/mnt/ez.net/chall/bin/Release/net7.0/re-1.dll");

var partial_flag = new byte[]{
    0x6d,0x6f,0x65,0x63,0x74,0x66
};

var magic_type = assembly.GetType("KoitoCoco.MoeCtf.KoitoMagicalShop") ?? throw new NotImplementedException();
var magic_field = magic_type.GetField("MagicalDust", BindingFlags.Static |BindingFlags.Public) ?? throw new NotImplementedException();

var catfood = new byte[][]{
    Encoding.UTF8.GetBytes("Meow~!?!"),
    Encoding.UTF8.GetBytes("meoW?!~~"),
    Encoding.UTF8.GetBytes("me0w~?!!"),
    Encoding.UTF8.GetBytes("mEow????")
};

foreach (var type in assembly.GetTypes())
{
    if (type.Name.StartsWith("FlagMachine_"))
    {
        Console.WriteLine("Try type: " + type.Name);
        foreach (var param in catfood)
        {
            try
            {
                var instance = Activator.CreateInstance(type);
                var set_flag = type.GetMethod("SetFlag");
                set_flag!.Invoke(instance, new object[] { param });
                var get_flag = type.GetMethod("VmeFlag");
                get_flag!.Invoke(instance, new object[] { "\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0" });
                if (magic_field.GetValue(null!) is int[] flag)
                {
                    bool check = true;
                    for (int i = 0; i < 6; i++)
                    {
                        if (flag[i] != partial_flag[i])
                        {
                            check = false;
                            break;
                        }
                    }
                    if (!check)
                    {
                        continue;
                    }
                    var flag_str = Encoding.UTF8.GetString(flag.Select(x => (byte)x).ToArray());
                    Console.WriteLine(flag_str);
                    return;
                }
                else
                {
                    Console.WriteLine("Failed to get field");
                }
            }
            catch (System.Exception ex)
            {
                System.Console.WriteLine(ex);
                return;
            }
        }
    }
}