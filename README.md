# Freedom Songs

Community curated database of songs of the movement by popular artists of color.


### Current Routes
|Verb |Path   |Return   |Use   |Auth |
|---|---|---|---|:---:|
|GET|/|render:`home.html`|Homepage for all visitors|N|
|GET|/faq|render:`faq.html`|FAQ page|N|
|GET|/about|render:`about.html`|About page|N|
|GET|/users/signup|render:`signup.html`|Signup Form|N|
|POST|/users/signup|redirect:`home.html`|Account creation|N|
|GET|/users/login|render:`login.html`|Login page|N|
|POST|/users/login|redirect:`home.html`|Authenticates user|Y|
|GET|/users/logout|redirect:`users.login`|Logs out user|Y|
|DELETE|/users/\<user_id>|redirect:`home.html`|Deletes account|Y|
|GET|/users/\<user_id>/song/new|render:`new.html`|Submit a new song|Y|
|POST|/users/\<user_id>/song/new|redirect:`home.html`|Submit a new song|Y|


### Future Functionality
|Verb |Path   |Return   |Use   |Auth |
|---|---|---|---|:---:|
|GET|/users/\<user_id>/account|render:`account.html`|Display account preferences|Y|
|PATCH|/users/\<user_id>|redirect:`account.html`|Updates user information|Y|
|GET|/users/\<admin>|render:`admin.html`|Special route for me!|Y+|
|GET|/users/\<user_id>/blog|render:`blog.html`|Display user's public blog|N|
|GET|/users/\<user_id>/blog/new|render:`new_post.html`|Submit new blog post for review |Y|
|GET|/users/\<user_id>/blog/post/\<post\_id>|render:`post.html`|Display specific post|N|
