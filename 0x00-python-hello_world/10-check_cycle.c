#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - hecks if a singly linked list has a cycle in it.
 * @list: pointer  to list to be check
 * Retunr: int 0 if no cycle and 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
    listint_t *slow = list;
    listint_t *fast = list;

    while (fast != NULL && fast->next != NULL)
    {
        slow = slow->next;

        fast = fast->next->next;

        if (slow == fast) {
            return 1;
        }
    }

    return 0;
}