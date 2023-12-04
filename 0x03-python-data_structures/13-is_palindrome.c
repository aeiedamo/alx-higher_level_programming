#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

int is_palindrome(listint_t **head)
{
    listint_t *compare = *head;

    if (!head || !*head || !compare)
        return (1);
    
    do
    {
        if (((*head)->n != compare->n))
            return (0);
        *head = (*head)->next;
    } while (compare->next);

    return (1);
    
}