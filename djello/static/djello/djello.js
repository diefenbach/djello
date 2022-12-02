function createSortable(list_id) {
    for (const el of document.querySelectorAll('.dj-list')) {
        // If list_id is given only for this list Sortable is created.
        // This is used after the list has been swapped.
        if (list_id && "list-id-" + list_id !== el.getAttribute("id")) {
            continue;
        }

        Sortable.create(el, {
            group: 'shared',
            animation: 150,
            store: {
                set: function (sortable) {
                    const ar = sortable.toArray()
                    if (ar.length > 0) {
                        const el = document.querySelector("[data-id='" + ar[0] + "']")
                        const list_id = el.parentElement.getAttribute("data-id");
                        const params = {
                            method: "POST",
                            body: JSON.stringify({
                                "list": list_id,
                                "cards": ar,
                            }),
                        }
                        fetch(dj_store_lists_url, params).then();
                    }
                }
            }
        });
    }
}

createSortable()
