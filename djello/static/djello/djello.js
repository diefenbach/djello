const sortables = []
htmx.onLoad(
    // this will be called whenever something swapped in.
    function createSortable() {
        // First remove all sortables
        for (const sortableElement of sortables) {
            try { sortableElement.destroy() } catch {}
        }

        // Then create fresh ones
        for (const el of document.querySelectorAll('.dj-list')) {
            const sortable = Sortable.create(el, {
                group: 'shared',
                animation: 150,
            });

            sortables.push(sortable);
        }
    }
);
