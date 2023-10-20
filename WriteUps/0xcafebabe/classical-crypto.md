# Classical-Crypto
### Author: 0xcafebabe

## CHALLENGE: caesar
```题目给出
tvljam{JhLzhL_JPwoLy_Pz_h_cLyF_zPtwPL_JPwoLy!_ZmUVUA40q5KbEQZAK5Ehag4Av}
```
显然提示了凯撒密码，所以在CyberChef上使用ROT13进行解密

https://cyberchef.org/#recipe=ROT13(true,true,false,-7)&input=dHZsamFte0poTHpoTF9KUHdvTHlfUHpfaF9jTHlGX3pQdHdQTF9KUHdvTHkhX1ptVVZVQTQwcTVLYkVRWkFLNUVoYWc0QXZ9

```
flag: moectf{CaEsaE_CIphEr_Is_a_vErY_sImpIE_CIphEr!_SfNONT40j5DuXJSTD5Xatz4To}
```
---

## CHALLENGE: ezrot
```题目给出 @64E7LC@Ecf0:D0;FDE020D:>!=60=6EE6C0DF3DE:EFE:@?04:!96C0tsAJdEA6d;F}%0N```

由于提示了ROT，所以操作一样，注意ROT13不换@符号，所以使用ROT47，从而得到flag

https://cyberchef.org/#recipe=ROT47(47)&input=QDY0RTdMQ0BFY2YwOkQwO0ZERTAyMEQ6PiE9NjA9NkVFNkMwREYzREU6RUZFOkA/MDQ6ITk2QzB0c0FKZEVBNmQ7Rn0lME4

---

## CHALLENGE: fence
```
题目给出了fences，所以是栅栏密码
mt3_hsTal3yGnM_p3jocfFn3cp3_hFs3c_3TrB__i3_uBro_lcsOp}e{ciri_hT_avn3Fa_j
```

```
随便调一下，发现在key = 3 , Offset = 0得到flag
```

https://cyberchef.org/#recipe=Rail_Fence_Cipher_Decode(3,0)&input=bXQzX2hzVGFsM3lHbk1fcDNqb2NmRm4zY3AzX2hGczNjXzNUckJfX2kzX3VCcm9fbGNzT3B9ZXtjaXJpX2hUX2F2bjNGYV9q

---

## CHALLENGE: morse
### 没做出来，因为当时以为一个字符对应一个-或者.，后来看到别人的WP才恍然大悟
```
喵喵？ -> .
喵喵喵 -> -
```

```
. ---- - --..-. .-. -. -.. -. -- -- --..-. .-.- -. . --..-. .--- --. . --..-. .--- - --..-. .-.- -. -.-- -.-- - .-- --..-. ..- ... --. ..-- -- --..-. .--- .-.. --..-. -.- .--.
```

https://cyberchef.org/#recipe=From_Morse_Code('Space','Line%20feed')&input=LiAtLS0tIC0gLS0uLi0uIC4tLiAtLiAtLi4gLS4gLS0gLS0gLS0uLi0uIC4tLi0gLS4gLiAtLS4uLS4gLi0tLSAtLS4gLiAtLS4uLS4gLi0tLSAtIC0tLi4tLiAuLS4tIC0uIC0uLS0gLS4tLSAtIC4tLSAtLS4uLS4gLi4tIC4uLiAtLS4gLi4tLSAtLSAtLS4uLS4gLi0tLSAuLS4uIC0tLi4tLiAtLi0gLi0tLg

最后加上moectf{}即可


## CHALLENGE: vigenere

```
题目给出：
scsfct{wOuSQNfF_IWdkNf_Jy_o_zLchmK_voumSs_zvoQ_loFyof_FRdiKf_4i4x4NLgDn}

md5 of flag (utf-8) ea23f80270bdd96b5fcd213cae68eea5
```

根据提示，找到vigenere Decode，发现要拿key解密，而且只能是字母密码。我们发现密码后面的位不影响前面，所以我们大胆尝试挨个破解，分别使得前六个字符是moectf即可
```
key = "g"
decode = "mwmzwn{qIoMKHzZ_CQxeHz_Ds_i_tFwbgE_piogMm_tpiK_fiZsiz_ZLxcEz_4c4r4HFaXh}"
```

```
key = "go"
decode = "momrwf{qAoEKZzR_CIxwHr_Dk_i_lFobyE_higgEm_lpaK_xiRsaz_RLpcWz_4u4r4ZFsXz}"
``````

```
key = "goo"
decode = "moezof{qAgMCZzR_UQpwHr_Vs_a_lFotgW_higyMe_lpaC_faRsar_ZDpcWr_4c4j4ZFsPh}"
``````

```
key = "good"
decode = "moecwf{iLoECKzR_UTxwZc_Dk_a_wFotjE_hargEe_wpaC_iiRklz_RDacWr_4f4r4ZXdXz}"
``````

```
key = "goodjo"
decode = "moectf{qAgPHZzR_UTuwHr_Vv_f_lFotjB_higyPj_lpaC_ifRsar_CIpcWr_4f4o4ZFsPk}"
``````

最后由我的poor english 得到key = "goodjob"

```
观察到有明显的单词，就说明大概率对了
moectf{vIgENErE_CIphEr_Is_a_lIttlE_hardEr_thaN_caEsar_CIphEr_4u4u4EXfXz}
```