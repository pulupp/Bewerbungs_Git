#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

#define MAX_TEXT_LENGTH 1000

int main(void)
{
    char text[MAX_TEXT_LENGTH];
    //ask for user input
    printf("Text: ");
        if (fgets(text, MAX_TEXT_LENGTH, stdin) == NULL){
            printf("Error reading input.\n");
            return 1;
        };

    //count word length and scentence length
    int word_count = 0;
    int sentence_count = 0;
    int total_word_length = 0;
    int total_sentence_length = 0;

    char *word = strtok(text, " ");
    while (word != NULL) {
        word_count++;
        total_word_length += strlen(word);
        word = strtok (NULL, " ");

    }

    // reset the pointer to the beginning of the string
    char *text_ptr = text;
    char *sentence = strtok(text, ".");
    while (sentence != NULL) {
        if ( sentence[strlen(sentence) - 1] == ' ' || sentence[strlen(sentence) - 1] == '\0'){
            sentence_count++;
            total_sentence_length += strlen(sentence);
        }
        sentence = strtok(NULL, ".");

    }

    double average_word_length = (double)total_word_length / word_count;
    double average_sentence_length = (double)total_sentence_length / sentence_count;
        //compute the coleman-index of the scentence and words

    double index  = 0.0588 * average_word_length - 0.296 * average_sentence_length - 15.8;

        //make an if statement to categorize the readability to each grade
            //if readability < 1 readability = before School
            //else if readability < 2 readability = firstgrade and so on

    char *readability_grade;
    if (index < 1 ) {
        readability_grade = "before School";
    }   else if (index < 2 ) {
        readability_grade = "first grade";
    }   else if (index < 3 ){
        readability_grade = "second grade";
    }   else if (index < 4 ) {
        readability_grade = "third grade";
    }   else if (index < 5 ){
        readability_grade = "fourth grade";
    }   else if (index < 6 ) {
        readability_grade = "fifth grade";
    }   else if (index < 7 ){
        readability_grade = "sixth grade";
    }   else if (index < 8 ) {
        readability_grade = "seventh grade";
    }   else if (index < 9 ){
        readability_grade = "eighth grade";
    }  else if (index < 10 ) {
        readability_grade = "ninth grade";
    }   else if (index < 11 ){
        readability_grade = "tenth grade";
    }   else if (index < 12 ) {
        readability_grade = "eleventh grade";
    }   else if (index < 13 ){
        readability_grade = "twelfth grade";
    }   else if (index < 14 ) {
        readability_grade = "thirteenth grade";
    }   else if (index < 15 ){
        readability_grade = "fourteenth grade";
    }   else if (index < 16 ) {
        readability_grade = "fifteenth grade";
    }   else {
           readability_grade = "sixteenth grade";
    }


        //promt output which readability grade the text has
    printf("%s\n", readability_grade);

    return 0;
}
