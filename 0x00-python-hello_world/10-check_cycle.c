#include "lists.h"

int check_cycle(listint_t *list)
{
	listint_t *chk;

	if (!list || !list->next)
		return (0);

	for (chk = list->next; 
		list && chk->next && chk->next->next; list = list->next,
		chk = chk->next->next)
	{
		if (list == chk)
			return (1);
	}

	return (0);
}