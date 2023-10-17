using System.Text;
using System.Diagnostics;
using static KoitoCoco.MoeCtf.CatFoodSeller;
namespace KoitoCoco.MoeCtf
{
    public static class CatFoodSeller
    {
        public static dynamic DoSomething()
        {
            j.ii1();
            j.iii1();
            var condition = j.i() || j.ii() || j.iii() || j.iii() || j.iiii() || j.i1();
            if (condition)
            {
                if (Process.GetCurrentProcess().ProcessName == "feed rx's cat")
                {
                    return "bad food";
                }
                else
                {
                    return null!;
                }
            }
            else
            {
                if (Process.GetCurrentProcess().ProcessName == "feed rx's cat")
                {
                    return new Exception("unexpected food");
                }
                else
                {
                    return new CatFood();
                }
            }
        }
    }
    public sealed class CatFood
    {
        public string Name { get; set; } = "Magic Cat Food";
        public string Brand { get; set; } = "Made in Heaven!";
        public int Price { get; set; } = 114514;

        public override string ToString()
        {
            return $"Name: {Name}, Brand: {Brand}, Price: {Price}";
        }

        public static implicit operator string(CatFood catFood)
        {
            return catFood.ToString();
        }
    }

    public static class CatOfRX
    {
        public static byte[] FeedCat(dynamic catFood)
        {
            if (catFood is null)
            {
                return Encoding.UTF8.GetBytes("Meow~!?!");
            }
            else
            {
                if (catFood is string catCan)
                {
                    if (catCan != catFood)
                    {
                        return Encoding.UTF8.GetBytes("meoW?!~~");
                    }
                    else
                    {
                        return Encoding.UTF8.GetBytes("me0w~?!!");
                    }
                }
                else
                {
                    return Encoding.UTF8.GetBytes("mEow????");
                }
            }
        }
    }

    public static class FlagHelper
    {
        static FlagHelper()
        {
            Console.WriteLine(Encoding.UTF8.GetString(Convert.FromBase64String("WW91IGhhdmUgZW50ZXJlZCBhIG5ldyB3b3JsZCE=")));
            AppDomain.CurrentDomain.UnhandledException += (sender, args) =>
            {
                Console.WriteLine(Encoding.UTF8.GetString(Convert.FromBase64String("U3VwZXJjYXQgaXMgdHJ5aW5nIHRvIHJlY292ZXIgeW91ISBidXQgaXQgaXMgaHVuZ3J5IQ==")));
                var a = DoSomething();
                Console.WriteLine(Encoding.UTF8.GetString(Convert.FromBase64String("b2ggbXkgZ29kISB3aGVyZSBhbSBpPz8/IGJ1dCBjYW4geW91IHYgbWUgNTAgdG8gZWF0IGtmYyBjcmF6eSB0aHVyc2RheT8gW1llcy9Ob10=")));
                var b = Console.ReadLine();
                var chosen = b!.Substring(7, 4);
                var inst = Activator.CreateInstance((from item in AppDomain.CurrentDomain.GetAssemblies() from type in item.GetTypes() where type.Name.EndsWith(chosen) select type).FirstOrDefault((i) => i.Name.Contains("FlagMachine"), typeof(FlagMachine)));
                if (inst is IFlagMachine fm)
                {
                    fm.SetFlag(CatOfRX.FeedCat(a));
                    fm.VmeFlag(b);
                }
                else
                {
                    Console.WriteLine(Encoding.UTF8.GetString(Convert.FromBase64String("aGV5IGJybywgdGhpcyBpcyBhIGZha2UgZmxhZyBtYWNoaW5lISB3ZSBhcmUgY2hlYXRlZCE=")));
                }
            };
        }
        public static string Flag = Encoding.UTF8.GetString(Convert.FromBase64String("bW9lY3Rme0QwX3kwVV82ZTFpZXZlX3RoYXRfdGhpc19pc190aGVfcmlHaHRfZjFhRz9faVlsSmYhTTNydXg5RzlWZiFKb3h9"));
    }

    public interface IFlagMachine
    {
        void SetFlag(dynamic flag);
        void VmeFlag(string token);
    }

    public static class KoitoMagicalShop
    {
        public static int[] Params = new int[8];
        public static int[] States = new int[512];
        public static void ResetState(byte[] p)
        {
            var init = new int[512] { 132, 115, 194, 131, 143, 106, 94, 242, 84, 205, 131, 226, 54, 207, 228, 31, 195, 182, 56, 229, 129, 238, 167, 94, 103, 201, 94, 4, 123, 249, 233, 211, 138, 83, 64, 40, 161, 148, 35, 95, 10, 234, 200, 132, 110, 74, 143, 148, 31, 214, 123, 34, 125, 170, 245, 185, 218, 178, 172, 151, 80, 105, 101, 200, 92, 20, 127, 168, 49, 231, 63, 111, 53, 0, 152, 28, 163, 169, 4, 171, 66, 164, 51, 119, 86, 81, 75, 81, 115, 121, 167, 80, 88, 116, 99, 118, 132, 119, 121, 15, 94, 68, 100, 27, 14, 89, 106, 145, 52, 12, 8, 21, 2, 232, 106, 121, 157, 167, 102, 19, 94, 254, 155, 38, 0, 108, 109, 166, 21, 220, 54, 209, 41, 74, 17, 25, 28, 171, 137, 208, 179, 7, 182, 55, 145, 195, 54, 46, 4, 192, 52, 242, 97, 90, 101, 241, 17, 176, 111, 42, 199, 250, 37, 238, 160, 106, 192, 9, 68, 222, 225, 142, 208, 226, 217, 70, 14, 166, 54, 102, 90, 28, 163, 169, 54, 209, 43, 163, 183, 102, 11, 98, 22, 142, 113, 25, 86, 220, 60, 78, 5, 29, 69, 93, 166, 183, 71, 167, 33, 228, 210, 204, 20, 33, 155, 67, 139, 88, 40, 18, 137, 150, 250, 31, 250, 69, 147, 4, 28, 121, 4, 205, 198, 113, 229, 234, 14, 15, 217, 250, 164, 162, 237, 176, 109, 29, 171, 225, 28, 17, 213, 228, 226, 86, 111, 63, 146, 107, 81, 6, 140, 178, 9, 28, 35, 135, 118, 194, 170, 58, 126, 39, 52, 248, 77, 29, 72, 150, 69, 207, 75, 203, 191, 186, 207, 250, 14, 148, 142, 46, 178, 80, 8, 64, 240, 184, 128, 104, 245, 33, 26, 194, 185, 168, 183, 246, 189, 47, 70, 176, 117, 48, 150, 155, 34, 62, 227, 49, 198, 115, 160, 20, 199, 103, 169, 132, 76, 22, 229, 60, 111, 134, 3, 233, 151, 217, 190, 249, 63, 138, 119, 63, 211, 34, 13, 5, 73, 246, 192, 211, 16, 18, 241, 44, 254, 72, 71, 240, 189, 144, 255, 244, 238, 229, 235, 224, 50, 23, 173, 183, 165, 112, 26, 84, 48, 60, 94, 249, 180, 28, 193, 91, 59, 6, 217, 162, 240, 163, 102, 133, 78, 1, 100, 54, 40, 88, 234, 15, 104, 152, 115, 35, 84, 200, 246, 8, 204, 182, 125, 97, 110, 179, 106, 62, 110, 1, 192, 140, 199, 5, 82, 243, 204, 79, 66, 126, 254, 6, 23, 244, 206, 117, 33, 247, 204, 246, 105, 199, 62, 87, 153, 83, 140, 220, 127, 85, 177, 233, 22, 153, 1, 170, 31, 149, 212, 229, 113, 26, 40, 209, 31, 137, 123, 43, 121, 116, 87, 233, 123, 204, 231, 125, 18, 67, 239, 192, 155, 226, 133, 91, 137, 114, 181, 226, 94, 226, 231, 248, 107, 143, 204, 140, 215, 170, 227, 84, 142, 36, 118, 136, 250, 206, 121, 213, 24, 174, 148, 171, 78, 212, 32, 151 };
            for (int i = 0; i < 512; i++)
            {
                States[i] = init[i];
            }
            for (int i = 0; i < 8; i++)
            {
                Params[i] = p[i];
            }
            for (int i = 0; i < 233; i++)
            {
                GetNextSpellcard();
            }
        }
        public static byte GetNextSpellcard()
        {
            var current = 233;
            foreach (var item in Params)
            {
                current ^= States[item];
                unchecked
                {
                    current += 1;
                }
            }
            for (int i = 0; i < 511; i++)
            {
                States[i] = States[i + 1];
            }
            States[511] = current;
            return (byte)current;
        }
        public static bool IsRealFlag(byte[] flag, byte[] paramaters)
        {
            if (flag.Length != 72)
            {
                return false;
            }
            ResetState(paramaters);
            var MagicalFlag = new int[72]{143, 75, 130, 35, 251, 51, 51, 49, 92, 145, 151, 13, 30, 200, 47, 14, 231, 100, 49, 169, 56, 25, 94, 176, 116, 11, 128, 10, 186, 63, 185, 45, 216, 55, 190, 72, 130, 200, 139, 252, 58, 250, 37, 151, 179, 220, 200, 35, 111, 41, 100, 87, 203, 54, 7, 81, 59, 153, 165, 71, 255, 195, 220, 144, 112, 243, 227, 251, 228, 232, 246, 251};
            var mask = new int[72];
            for (int i = 0; i < 72; i++)
            {
                mask[i] ^= GetNextSpellcard();
            }
            for (int i = 0; i < 72; i++)
            {
                MagicalFlag[i] ^= (flag[i] ^ mask[i]);
            }
            MagicalDust = MagicalFlag;
            return MagicalFlag.All(i=>i == 0);
        }
        public static int[] MagicalDust = new int[72];
    }
}
