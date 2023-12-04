#include "lists.h"
/**
 * compare - function to compare nodes
 * @head: pointer to head node
 * @comp: pointer to compared node
 * Return: 1 if all previous comparisons were success, 0 otherwise
*/
int compare(listint_t **head, listint_t *comp)
{
	if (!comp)
		return (1);
	if (compare(head, comp->next) && (*head)->n == comp->n)
	{
		(*head) = (*head)->next;
		return (1);
	}
	return (0);
}

/**
 * is_palindrome - function to check if a list is palindrome
 * @head: pointer to head node
 * Return: 0 if list is not palindrome, 1 otherwise
*/

int is_palindrome(listint_t **head)
{
	if (!head || !(*head))
		return (1);
	return(compare(head, *head));
}