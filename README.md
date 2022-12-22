# djello
This is a try to create a trello clone by using Django, django_components, htmx and hyperscript.


## Goal
- Main focus at the moment is: Use django_components to render the whole content on the first request without the use of any Javascript (SEO) and to be able to refresh those components (easily) later without a whole page reload. 

- To prove that one can create a rich user interface without a complex javascript framework for the frontend and all the negative consequences it has, e.g. a REST API and its security/permission impacts. 

## Installation 
1. Clone this repository
2. Create and activate a virtual environment
3. pip install -r requirements.txt
4. python manage.py migrate
5. python manage.py runserver

## Contact
If you have any questions or suggestions, please don't hesitate to get in contact (kai.diefenbach@iqpp.de). I am very interested in your thoughts and approaches according to this topic.


## Further information
- django_components: https://github.com/EmilStenstrom/django-components/
- htmx: https://htmx.org/
- hyperscript: https://hyperscript.org/
- Real world example: https://www.youtube.com/watch?v=3GObi93tjZI&t=1s
- Article: https://arhamjain.com/2021/12/18/hyperscript-simple-type.html
- djhtmx, interactive UI Components for Django using htmx: https://github.com/edelvalle/djhtmx


## Thanks
- Thanks to the Russ Ferriday (russ.ferriday@gmail.com) who introduced me to django_components, htmx and hyperscript.
- And of course to the makers of Python, Django, django_components, htmx and hyperscript.
