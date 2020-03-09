/*
 * Build Your Own ECSC 2019 Team
 */
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include "byot.h"

#define MAX_PLAYERS 10
#define BUFSIZE 128

/* Global variables */
struct player *players[MAX_PLAYERS]; 
struct player *selected_player;

void print_main_menu()
{
    puts("-=== Build Your Own Team - ECSC 2019 edition! ===-");
    puts("1. Show the ECSC 2019 team");
    puts("2. Show player");
    puts("3. Select player");
    puts("4. Add new player");
    puts("5. Remove player");
    puts("6. Edit player");
    puts("7. Exit");
}

void print_edit_menu()
{
    puts("-= Edit selected user menu =-");
    puts("1. Edit name");
    puts("2. Set pwn skillz points");
    puts("3. Set crypto skillz points");
    puts("4. Set web skillz points");
    puts("5. Set stega skillz points");
    puts("6. Back to main menu");
}

void read_input(char *buf, unsigned int len)
{
  if(fgets(buf, len, stdin)) {
    char *p;
    if((p=strchr(buf, '\n'))) { //check exist newline
      *p = 0;
    } else {
      scanf("%*[^\n]"); scanf("%*c"); //clear upto newline
    }
  }
}

unsigned int edit_menu()
{
    char choice[4];

    print_edit_menu();
    printf("Please enter your choice: ");
    read_input(choice, 4);

    return atoi(choice);
}

unsigned int main_menu()
{
    char choice[4];

    print_main_menu(); 
    printf("Please enter your choice: ");
    read_input(choice, 4);

    return atoi(choice);
}

/* Edit currently selected player */
void edit_player()
{
    unsigned int choice;

    if (selected_player != NULL)
    {
        do
        {
            choice = edit_menu();
            switch(choice)
            {
                case 1:
                    set_name();
                    break;
                case 2:
                    set_pwn();
                    break;
                case 3:
                    set_crypto();
                    break;
                case 4:
                    set_web();
                    break;
                case 5:
                    set_stega();
                    break;
            }
        } while (choice >= 1 && choice <= 5);
    }
    puts("[-] No player currently selected");
}

/* Select a specific player */
void select_player()
{
    char buf[3];
    unsigned int index;

    puts("Enter the index of the player you would like to select: ");
    read_input(buf, 3);
    index = atoi(buf);
    if (index <= MAX_PLAYERS && players[index] != NULL)
    {
        selected_player = players[index];
        printf("Player at index %u is now selected!\n", index);
        print_player(selected_player);
    } 
    else
    {
        puts("[-] Invalid Index");
    }
}

/* Add a new player in a free slot, if available */
void add_player()
{
    unsigned int index;
    struct player *player;
    char buf[BUFSIZE];

    /* Find the next availabla slot */
    for (index = 0; index < MAX_PLAYERS && players[index] != NULL; index++)
        ;
    /* If index is 11, than we have no more available slot on the team */
    if (index == MAX_PLAYERS + 1)
    {
        printf("[-] Your team cannot have more than %u players!", MAX_PLAYERS);
    }
    else
    {
        printf("[!] Free slot at index %d\n", index);
        player = malloc(sizeof(struct player));
        if (player != NULL)
        {
            memset(player, 0, sizeof(struct player));
            puts("Enter player name: ");
            memset(buf, 0, BUFSIZE);
            read_input(buf, BUFSIZE);
            player->name = malloc(strlen(buf) + 1);

            if (player->name)
            {
                strcpy(player->name, buf);
                puts("Enter pwn skillz [1-999]: ");
                read_input(buf, 4);
                player->pwn = atoi(buf);
                puts("Enter crypto skillz [1-999]: ");
                read_input(buf, 4);
                player->crypto = atoi(buf);
                puts("Enter web skillz [1-999]: ");
                read_input(buf, 4);
                player->web = atoi(buf);
                puts("Enter stegoguess skillz [1-999]: ");
                read_input(buf, 4);
                player->stega = atoi(buf);
                /* Store the player into the global array */
                players[index] = player;
            }
            else
            {
                puts("[-] Allocation error: player name");
            }
        }
        else
        {
            puts("[-] Allocation error: player struct");
        }
    }

}

/* Remove a player from the team */
void remove_player()
{
    struct player *player;
    unsigned int index;
    char buf[4];

    puts("Enter the index of the player you would like to remove: ");
    read_input(buf, 4);
    index = atoi(buf);
    if (index <= MAX_PLAYERS && players[index] != NULL)
    {
        player = players[index];
        players[index] = NULL;
        free(player->name);
        free(player);
        printf("[*] Player at index %u has been removed from the team\n", index);
    }
    else
    {
        puts("[-] Invalid player index");
    }
}

/* Edit the name of the selected player */
void set_name()
{
    char newname[BUFSIZE];
    size_t old_len, new_len;
    char *newbuf;

    printf("Enter the new name for the selected player: ");
    read_input(newname, BUFSIZE);
    old_len = strlen(selected_player->name);
    new_len = strlen(newname);

    if (new_len <= old_len)
    {
        strcpy(selected_player->name, newname);
    }
    else
    {
        newbuf = (char *)realloc(selected_player->name, new_len + 1);
        if (newbuf != NULL)
        {
            selected_player->name = newbuf;
            strcpy(selected_player->name, newname);
        }
        else
        {
            puts("[-] Allocation error: realloc new name");
        }
    }


}

/* Set the pwn score for the selected player */
void set_pwn()
{
    struct player* player;
    char buf[4];

    printf("Enter pwn skillz [1-999]: ");
    read_input(buf, 4);
    player = selected_player;
    player->pwn = atoi(buf);
}

/* Set the crypto score for the selected player */
void set_crypto()
{
    struct player* player;
    char buf[4];

    printf("Enter crypto skillz [1-999]: ");
    read_input(buf, 4);
    player = selected_player;
    player->crypto = atoi(buf);
}

/* Set the web score for the selected player */
void set_web()
{
    struct player* player;
    char buf[4];

    printf("Enter web skillz [1-999]: ");
    read_input(buf, 4);
    player = selected_player;
    player->web = atoi(buf);
}

/* Set the stega score for the selected player */
void set_stega()
{
    struct player* player;
    char buf[4];

    printf("Enter stega skillz [1-999]: ");
    read_input(buf, 4);
    player = selected_player;
    player->stega = atoi(buf);
}


/* Print a specific player's characteristics */
void print_player(struct player* player)
{
    printf("Name: %s\n", player->name);
    printf("- Pwn:        %d\n", player->pwn);
    printf("- Crypto:     %d\n", player->crypto);
    printf("- Web:        %d\n", player->web);
    printf("- Stega:      %d\n", player->stega);
}

/* Show the currently selected player */
void show_player()
{
    if (selected_player != NULL)
    {
        print_player(selected_player);
    }
    else
    {
        puts("[-] No currently selected player");
    }
}

/* Show the whole team */
void show_team()
{
    struct player *player;
    unsigned int i = 0;

    puts("Behold! Here is your dream ECSC team!");
    for(i = 0; i < MAX_PLAYERS; i++)
    {
        player = players[i];
        if (player != NULL)
        {
            printf("Player #%d\n", i);
            print_player(players[i]);
        }
    }
}


int main()
{
    unsigned int choice;

    setvbuf(stdin,  NULL, _IONBF, 0); /* turn off buffering */
    setvbuf(stdout, NULL, _IONBF, 0); /* turn off buffering */

    do
    {
        choice = main_menu();
        switch(choice)
        {
            case 1:
                show_team();
                break;
            case 2:
                show_player();
                break;
            case 3:
                select_player();
                break;
            case 4:
                add_player();
                break;
            case 5:
                remove_player();
                break;
            case 6:
                edit_player();
                break;
        }
    } while (choice >= 1 && choice <= 6);

    puts("Bye!");
    exit(EXIT_SUCCESS);
}
