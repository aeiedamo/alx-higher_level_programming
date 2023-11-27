#include "lists.h"

int check_cycle(listint_t *list)
{
        listint_t *curr, *chk;

        if (!list || !list->next)
                return (0);

        for (curr = list, chk = curr->next; 
                curr && chk->next && chk->next->next; curr = curr->next,
                chk = chk->next->next)
        {
                if (curr == chk)
                        return (1);
                curr = curr->next;
                chk = chk->next->next;
        }

        return (0);
}