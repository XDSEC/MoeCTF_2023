#include <jni.h>
#include <string>
#include <android/log.h>
#include <stdbool.h>
#include <stdio.h>
#include <string.h>
char flag[30];
char maze[] =
    "***************"
    "***@******#****"
    "***.******.****"
    "*...******.****"
    "*.********.****"
    "*.****.....****"
    "*.****.********"
    "*......********"
    "***************"

    ;
int check_flag(const char* flag) {
  char* cur = (maze + 18);
  while (*flag && *cur != '*') {
    switch (*flag++) {
      case 'w':
        cur -= 15;
        break;
      case 's':
        cur += 15;
        break;
      case 'a':
        cur -= 1;
        break;
      case 'd':
        cur += 1;
        break;
      default:
        return 0;
    }
  }
  if (*cur == '#') {
    return 1;
  }
  return 0;
}

int not_check_flag2(const char* flag) {

char maze1[] =
    "***************"
    "**@************"
    "**..***********"
    "*...***********"
    "*.********..#**"
    "*.****.....****"
    "*.****.********"
    "*......********"
    "***************"

    ;
  char* cur = (maze1 + 17);
  while (*flag && *cur != '*') {
    switch (*flag++) {
      case 'w':
        cur -= 15;
        break;
      case 's':
        cur += 15;
        break;
      case 'a':
        cur -= 1;
        break;
      case 'd':
        cur += 1;
        break;
      default:
        return 0;
    }
  }
  if (*cur == '#') {
    return 1;
  }
  return 0;
}

int not_check_flag1(const char* flag) {

char maze1[] =
    "***************"
    "***@***********"
    "***.***********"
    "*...***********"
    "*.********...**"
    "*.****.....*#**"
    "*.****.********"
    "*......********"
    "***************"

    ;
  char* cur = (maze1 + 18);
  while (*flag && *cur != '*') {
    switch (*flag++) {
      case 'w':
        cur -= 15;
        break;
      case 's':
        cur += 15;
        break;
      case 'a':
        cur -= 1;
        break;
      case 'd':
        cur += 1;
        break;
      default:
        return 0;
    }
  }
  if (*cur == '#') {
    return 1;
  }
  return 0;
}

int not_check_flag3(const char* flag) {

char maze1[] =
    "***************"
    "***@***********"
    "***.***********"
    "*...***********"
    "*.********...#*"
    "*.****.....****"
    "*.****.********"
    "*......********"
    "***************"
    "***************"
    ;
  char* cur = (maze1 + 18);
  while (*flag && *cur != '*') {
    switch (*flag++) {
      case 'w':
        cur -= 15;
        break;
      case 's':
        cur += 15;
        break;
      case 'a':
        cur -= 1;
        break;
      case 'd':
        cur += 1;
        break;
      default:
        return 0;
    }
  }
  if (*cur == '#') {
    return 1;
  }
  return 0;
}

int not_check_flag4(const char* flag) {

char maze1[] =
    "***************"
    "***@***********"
    "***.***********"
    "*...***********"
    "*.*************"
    "*.****.....*#**"
    "*.****.***...**"
    "*......********"
    "***************"

    ;
  char* cur = (maze1 + 18);
  while (*flag && *cur != '*') {
    switch (*flag++) {
      case 'w':
        cur -= 15;
        break;
      case 's':
        cur += 15;
        break;
      case 'a':
        cur -= 1;
        break;
      case 'd':
        cur += 1;
        break;
      default:
        return 0;
    }
  }
  if (*cur == '#') {
    return 1;
  }
  return 0;
}
int not_check_flag5(const char* flag) {

char maze1[] =
    "***************"
    "***@***********"
    "***.***********"
    "*...***********"
    "*.*************"
    "*.****.....****"
    "*.****.***...#*"
    "*......********"
    "***************"

    ;
  char* cur = (maze1 + 18);
  while (*flag && *cur != '*') {
    switch (*flag++) {
      case 'w':
        cur -= 15;
        break;
      case 's':
        cur += 15;
        break;
      case 'a':
        cur -= 1;
        break;
      case 'd':
        cur += 1;
        break;
      default:
        return 0;
    }
  }
  if (*cur == '#') {
    return 1;
  }
  return 0;
}
int not_check_flag(const char* flag) {

char maze1[] =
    "***************"
    "***@***********"
    "***.***********"
    "*...***********"
    "*.********...#*"
    "*.****.....****"
    "*.****.********"
    "*......********"
    "***************"

    ;
  char* cur = (maze1 + 18);
  while (*flag && *cur != '*') {
    switch (*flag++) {
      case 'w':
        cur -= 15;
        break;
      case 's':
        cur += 15;
        break;
      case 'a':
        cur -= 1;
        break;
      case 'd':
        cur += 1;
        break;
      default:
        return 0;
    }
  }
  if (*cur == '#') {
    return 1;
  }
  return 0;
}



static jint JNICALL check(JNIEnv *env, jobject jobj, jstring input){
     const char *str = (env)->GetStringUTFChars(input, 0);
     char cap[128];
     env->ReleaseStringUTFChars(input, str);
    int result  = check_flag(str);

    return result;
}
static const JNINativeMethod gMethods[] = {
        {"check", "(Ljava/lang/String;)I", (jint *)check},
};


static jclass myClass;
static const char* const className="com/doctor3/ezandroid/MainActivity";
JNIEXPORT jint JNICALL JNI_OnLoad(JavaVM* vm, void* reserved){
    char true_maze[] =
    "***************"
    "***@***********"
    "***.***********"
    "*...****#..****"
    "*.********.****"
    "*.****.....****"
    "*.****.********"
    "*......********"
    "***************"

    ;
    memcpy(maze,true_maze,strlen(true_maze));
    JNIEnv* env = NULL;
    jint result = -1;
    if(vm->GetEnv((void **) &env, JNI_VERSION_1_4) != JNI_OK) {
        return -1;
    }
    myClass = env->FindClass(className);
    if(myClass == NULL)
    {
      return -1;
    }
    if(env->RegisterNatives(myClass, gMethods, sizeof(gMethods)/sizeof(gMethods[0])) < 0)
    {
      return -1;
    }
    return JNI_VERSION_1_4;
}


