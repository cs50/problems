#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main(int argc, string argv[])
{
 int main(int argc, char *argv[]) {
    // Make sure program was run with just one command-line argument
if (argc != 2) {
        printf("Usage: %s key\n", argv[0]);
        return 1; // Indicate an error
    }
    // Make sure every character in argv[1] is a digit
int main(void)
{   bool only_digits(string s)
    char c = get_char("Input: ");
    if (isdigit(c))
    {
        printf("Your input is a digit.\n");
    }
    else
    {
        printf("Your input is not a digit.\n");
    }
}
    }
    return ch; // If not an alphabet letter, return the character as is
}
    // Convert argv[1] from a 'string' to an 'int'
int key = atoi(argv[1]); // Ensure the key is within the range of 0 to 25 to avoid unnecessary large shifts
    key %= 26;
    // Prompt user for plaintext

    char plaintext[100]; // Declare a character array to store the plaintext

    printf("Enter plaintext: ");
    fgets(plaintext, sizeof(plaintext), stdin); // Read the plaintext from the user

    plaintext[strcspn(plaintext, "\n")] = 0;     // Remove the newline character if it exists in the input

    printf("Ciphertext: ");
    // For each character in the plaintext;
for (int i = 0; plaintext[i] != '\0'; i++) 
{
        // Encrypt the character using the caesar_encrypt_char function
        char encrypted_char = caesar_encrypt_char(plaintext[i], key);
        printf("%c", encrypted_char); // Print the encrypted character
}
printf("\n");
   
return 0; // Indicate successful execution
}
        // Rotate the character if its a letter
    char rotate(char c, int n);
    rotate('A', 1)
}
