/*
 * Build Your Own ECSC Team
 */
#ifndef BYOT_H
#define BYOT_H

struct player {
    unsigned int pwn;
    unsigned int crypto;
    unsigned int web;
    unsigned int stega;
    char *name;
};

void print_main_menu();
void print_edit_menu();
void read_input(char *, unsigned int);
unsigned int edit_menu();
unsigned int main_menu();
void edit_player();
void set_name();
void set_pwn();
void set_crypto();
void set_web();
void set_stega();
void select_player();
void add_player();
void remove_player();
void print_player(struct player *);
void show_player();
void show_team();

#endif //BYOT_H
