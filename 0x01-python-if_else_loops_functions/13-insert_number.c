#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *check = *head;
	listint_t *new;

	new = malloc(sizeof(listint_t));
	if (!head || !new)
		return (NULL);
	new->n = number;
	do
	{
		if (!check || check->n >= number)
		{
			new->next = check;
			*head = new;
			return (new);
		}
		check = check->next;
	} while (check && check->next && check->next->n < number);

	new->next = check->next;
	check->next = new;
	return (new);
}
