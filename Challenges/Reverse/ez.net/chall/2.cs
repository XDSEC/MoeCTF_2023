using System.Text;
namespace KoitoCoco.MoeCtf
{
    public static class Xorrrrr
    {
        public static dynamic xor(this byte[] bytes, ulong num)
        {
            var result = new byte[bytes.Length];
            for (int i = 0; i < bytes.Length; i++)
            {
                result[i] = (byte)(bytes[i] ^ (num >> (i % 8 * 8)));
            }
            return result;
        }
        public static dynamic xor(this ulong num, byte[] bytes)
        {
            var result = new byte[bytes.Length];
            for (int i = 0; i < bytes.Length; i++)
            {
                result[i] = (byte)(bytes[i] ^ (num >> (i % 8 * 8)));
            }
            return BitConverter.ToUInt64(result);
        }
    }
    public class FlagMachine : IFlagMachine
    {
        protected dynamic Flag;
        public virtual void SetFlag(dynamic flag)
        {
            this.Flag = BitConverter.GetBytes(flag);
        }
        public virtual void VmeFlag(string token)
        {
            Console.WriteLine("O-oooooooooo");
        }
    }

    public class YetAnotherFlagMachine : FlagMachine
    {
        public override void SetFlag(dynamic flag)
        {
            base.SetFlag((ulong)flag ^ 0xc0de_c0de_c0de_c0de);
        }
        public override void VmeFlag(string token)
        {
            Console.WriteLine("AAAAE-A-A-I-A-U- JO-oooooooooooo");
        }
    }
    public class ButAnotherFlagMachine : FlagMachine
    {
        public override void SetFlag(dynamic flag)
        {
            base.SetFlag((ulong)flag ^ 0x1551_1551_1551_1551);
        }
        public override void VmeFlag(string token)
        {
            Console.WriteLine("AAE-O-A-A-U-U-A- E-eee-ee-eee");
        }
    }
    public class FakeFlagMachine : YetAnotherFlagMachine
    {
        public override void SetFlag(dynamic flag)
        {
            base.SetFlag((ulong)flag ^ 0xa1b2_c3d4_e5f6_7890);
        }
        public override void VmeFlag(string token)
        {
            base.VmeFlag(token);
            if (KoitoMagicalShop.IsRealFlag(Encoding.UTF8.GetBytes(token), this.Flag))
            {
                Console.WriteLine("Good Job!");
            }
        }
    }
    public class FakeFlagMachinePlus : ButAnotherFlagMachine
    {
        public override void SetFlag(dynamic flag)
        {
            base.SetFlag((ulong)flag ^ 0x7890_a1b2_c3d4_e5f6);
        }
        public override void VmeFlag(string token)
        {
            base.VmeFlag(token);
            if (KoitoMagicalShop.IsRealFlag(Encoding.UTF8.GetBytes(token), this.Flag))
            {
                Console.WriteLine("Good Job!");
            }
        }
    }
    public class RealFlagMachine : ButAnotherFlagMachine
    {
        public override void SetFlag(dynamic flag)
        {
            base.SetFlag((ulong)flag ^ 0x7890_c3d4_a1b2_e5f6);
        }
        public override void VmeFlag(string token)
        {
            base.VmeFlag(token);
            if (KoitoMagicalShop.IsRealFlag(Encoding.UTF8.GetBytes(token), this.Flag))
            {
                Console.WriteLine("Good Job!");
            }
        }
    }
    public class RealFlagMachinePlus : YetAnotherFlagMachine
    {
        public override void SetFlag(dynamic flag)
        {
            base.SetFlag((ulong)flag ^ 0xc3d4_a1b2_e5f6_7890);
        }
        public override void VmeFlag(string token)
        {
            base.VmeFlag(token);
            if (KoitoMagicalShop.IsRealFlag(Encoding.UTF8.GetBytes(token), this.Flag))
            {
                Console.WriteLine("Good Job!");
            }
        }
    }
    public class FlagMachine_good : FakeFlagMachine
    {
        public override void SetFlag(dynamic flag)
        {
            base.SetFlag(BitConverter.ToUInt64((byte[])flag) + 0x1051_1551_1551_1591);
        }
    }
    public class FlagMachine_gooD : FakeFlagMachine
    {
        public override void SetFlag(dynamic flag)
        {
            base.SetFlag(BitConverter.ToUInt64((byte[])flag) + 0x1501_1551_1551_1951);
        }
    }
    public class FlagMachine_goOd : FakeFlagMachinePlus
    {
        public override void SetFlag(dynamic flag)
        {
            base.SetFlag(BitConverter.ToUInt64((byte[])flag) + 0x1551_0551_1559_1551);
        }
    }
    public class FlagMachine_goOD : FakeFlagMachinePlus
    {
        public override void SetFlag(dynamic flag)
        {
            base.SetFlag(BitConverter.ToUInt64((byte[])flag) + 0x1550_1551_1551_9551);
        }
    }
    public class FlagMachine_gOod : RealFlagMachinePlus
    {
        public override void SetFlag(dynamic flag)
        {
            base.SetFlag(BitConverter.ToUInt64((byte[])flag) + 0x1551_1051_1591_1551);
        }
    }
    public class FlagMachine_gOoD : RealFlagMachinePlus
    {
        public override void SetFlag(dynamic flag)
        {
            base.SetFlag(BitConverter.ToUInt64((byte[])flag) + 0x1551_1501_1951_1551);
        }
    }
    public class FlagMachine_gOOd : RealFlagMachine
    {
        public override void SetFlag(dynamic flag)
        {
            base.SetFlag(BitConverter.ToUInt64((byte[])flag) + 0x1551_1550_9551_1551);
        }
    }
    public class FlagMachine_gOOD : RealFlagMachine
    {
        public override void SetFlag(dynamic flag)
        {
            base.SetFlag(BitConverter.ToUInt64((byte[])flag) + 0x1551_1559_0551_1551);
        }
    }
    public class FlagMachine_Good : FlagMachine_good
    {
        public override void SetFlag(dynamic flag)
        {
            base.SetFlag((byte[])flag);
            this.Flag = Xorrrrr.xor(this.Flag,0x1145_1419_1981_0000);
        }
    }
    public class FlagMachine_GooD : FlagMachine_gooD
    {
        public override void SetFlag(dynamic flag)
        {
            base.SetFlag((byte[])flag);
            this.Flag = Xorrrrr.xor(this.Flag,0x1145_1419_1981_0000);
        }
    }
    public class FlagMachine_GoOd : FlagMachine_goOd
    {
        public override void SetFlag(dynamic flag)
        {
            base.SetFlag((byte[])flag);
            this.Flag = Xorrrrr.xor(this.Flag,0x1145_1419_1981_0000);
        }
    }
    public class FlagMachine_GoOD : FlagMachine_goOD
    {
        public override void SetFlag(dynamic flag)
        {
            base.SetFlag((byte[])flag);
            this.Flag = Xorrrrr.xor(this.Flag,0x1145_1419_1981_0000);
        }
    }
    public class FlagMachine_GOod : FlagMachine_gOod
    {
        public override void SetFlag(dynamic flag)
        {
            base.SetFlag((byte[])flag);
            this.Flag = Xorrrrr.xor(this.Flag,0x1145_1419_1981_0000);
        }
    }
    public class FlagMachine_GOoD : FlagMachine_gOoD
    {
        public override void SetFlag(dynamic flag)
        {
            base.SetFlag((byte[])flag);
            this.Flag = Xorrrrr.xor(this.Flag,0x1145_1419_1981_0000);
        }
    }
    public class FlagMachine_GOOd : FlagMachine_gOOd
    {
        public override void SetFlag(dynamic flag)
        {
            base.SetFlag((byte[])flag);
            this.Flag = Xorrrrr.xor(this.Flag,0x1145_1419_1981_0000);
        }
    }
    public class FlagMachine_GOOD : FlagMachine_gOOD
    {
        public override void SetFlag(dynamic flag)
        {
            base.SetFlag((byte[])flag);
            this.Flag = Xorrrrr.xor(this.Flag,0x1145_1419_1981_0000);
        }
    }
}