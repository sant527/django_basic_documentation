   * [<span>Basic </span><span>Django</span><span> Setup Documentation:</span>](#basic-djangosetup-documentation)
   * [<span>GOAL OF THIS PROJECT:</span>](#goal-of-this-project)
      * [<span>Session based Login using email and OTP and covering the basic django setup required</span>](#session-based-login-using-email-and-otp-and-covering-the-basic-django-setup-required)
         * [<span>[image] Home Page</span>](#image-home-page)
         * [<span>[image] Email form</span>](#image-email-form)
         * [<span>[image] OTP form</span>](#image-otp-form)
         * [<span>[image] Login confirmation and back to home page</span>](#image-login-confirmation-and-back-to-home-page)
         * [<span>[image] Logout confirmation and back to home page</span>](#image-logout-confirmation-and-back-to-home-page)
   * [<span>DOCUMENTATION START</span>](#documentation-start)
   * [<span>NEVER DO FIRST MIGRATION WITHOUT CREATING A CUSTOM “USER” MODEL and setting AUTH_USER_MODEL = custom_user.User in Settings.py</span>](#never-do-first-migration-without-creating-a-custom-user-model-and-setting-auth_user_model--custom_useruser-in-settingspy)
   * [<span>NEVER UPGRADE POSTGRESQL WITHOUT TAKING BACKUP. </span>](#never-upgrade-postgresql-without-taking-backup-)
   * [<span>TAKING BACKUP OF ENTIRE POSTGRESQL DATABASES</span>](#taking-backup-of-entire-postgresql-databases)
   * [<span>README MAKING for </span><span>Github Documentation using google doc to MarkDown:</span>](#readme-making-for-github-documentation-using-google-doc-to-markdown)
      * [<span>[code] Follow the below steps to convert to README.md with TOC and indenting</span>](#code-follow-the-below-steps-to-convert-to-readmemd-with-toc-and-indenting)
      * [<span>[image]( Commands to convert google.doc to markdown)</span>](#image-commands-to-convert-googledoc-to-markdown)
      * [<span>[code] View the .md file using grip</span>](#code-view-the-md-file-using-grip)
      * [<span>[code] Important Note about Images &amp;&amp; Split long images into smaller chunks (Because google docs reduce the image quality if images are big size)</span>](#code-important-note-about-images--split-long-images-into-smaller-chunks-because-google-docs-reduce-the-image-quality-if-images-are-big-size)
      * [<span>PROCEDURE IN IMAGES</span>](#procedure-in-images)
         * [<span>[image] Create a Sample_doc file using google docs as follows:</span>](#image-create-a-sample_doc-file-using-google-docs-as-follows)
         * [<span>[image] After saving the google doc Download it as web_page (html_zipped)</span>](#image-after-saving-the-google-doc-download-it-as-web_page-html_zipped)
         * [<span>[image] Extract the files into a folder</span>](#image-extract-the-files-into-a-folder)
         * [<span>[image] Open a Terminal and go to this folder and run the below command</span>](#image-open-a-terminal-and-go-to-this-folder-and-run-the-below-command)
         * [<span>[image] To view the .md file we use the grip command</span>](#image-to-view-the-md-file-we-use-the-grip-command)
         * [<span>[image] open </span><span><a href="https://www.google.com/url?q=http://localhost:6419/&amp;sa=D&amp;ust=1571383143923000" rel="nofollow">http://localhost:6419/</a></span><span> in browser</span>](#image-open-httplocalhost6419in-browser)
      * [<span>How to take screenshot of code from sublime text:</span>](#how-to-take-screenshot-of-code-from-sublime-text)
      * [<span>How to create a diff file for file between two commits</span>](#how-to-create-a-diff-file-for-file-between-two-commits)
         * [<span>[image] input (test.py) obtained from diff</span>](#image-input-testpy-obtained-from-diff)
         * [<span>[code] convertig to   to     and - to ---</span>](#code-convertig-to--to--and---to----)
         * [<span>[image] awk script</span>](#image-awk-script)
         * [<span>[image] output (test.py after running the above script) we added     and ---</span>](#image-output-testpy-after-running-the-above-script-we-added--and----)
   * [<span>FIRST COMMIT START:  </span>](#first-commit-start-)
      * [1.<span>We are using archlinux os and trying to setup a django project</span>](#1we-are-using-archlinux-os-and-trying-to-setup-a-django-project)
      * [2.<span>Installation pipenv:</span>](#2installation-pipenv)
         * [1.<span>[code] Change or login to root</span>](#1code-change-or-login-to-root)
         * [2.<span>[code] Install pipenv</span>](#2code-install-pipenv)
      * [3.<span>Create a project directory and change into it</span>](#3create-a-project-directory-and-change-into-it)
         * [1.<span>[code] Create main project directory</span>](#1code-create-main-project-directory)
         * [2.<span>[code] Change into project directory</span>](#2code-change-into-project-directory)
      * [4.<span>Create a virtual env inside the project directory using pipenv</span>](#4create-a-virtual-env-inside-the-project-directory-using-pipenv)
         * [1.<span>Set PIPENV_VENV_IN_PROJECT=1</span>](#1set-pipenv_venv_in_project1)
            * [<span>[code]</span>](#code)
         * [2.<span>[code] create virtualenv and activate it</span>](#2code-create-virtualenv-and-activate-it)
         * [3.<span>[code] Checking the files in the folder Pipfile is created</span>](#3code-checking-the-files-in-the-folder-pipfile-is-created)
      * [5.<span>In virtual env install Django</span>](#5in-virtual-env-install-django)
         * [1.<span>[code] Install Django</span>](#1code-install-django)
         * [2.<span>[code] Checking the files in the folder Pipfile is created</span>](#2code-checking-the-files-in-the-folder-pipfile-is-created)
         * [3.<span>[code] Checking the packages installed by pipenv</span>](#3code-checking-the-packages-installed-by-pipenv)
         * [4.<span>[code] Activating python virtualenv. From the path of the directory pipenv know which virtualenv to activate. So go to the directory and run the below command</span>](#4code-activating-python-virtualenv-from-the-path-of-the-directory-pipenv-know-which-virtualenv-to-activate-so-go-to-the-directory-and-run-the-below-command)
      * [6.<span>Check the version of Django</span>](#6check-the-version-of-django)
         * [1.<span>[code] Check the django version</span>](#1code-check-the-django-version)
      * [7.<span>Check the version of django-admin</span>](#7check-the-version-of-django-admin)
         * [1.<span>[code] If you get the below error then exit the virtualenv and again activate the virtualenv</span>](#1code-if-you-get-the-below-error-then-exit-the-virtualenv-and-again-activate-the-virtualenv)
         * [2.<span>[code] If you get the above error: exit and reactivate the virtualenv</span>](#2code-if-you-get-the-above-error-exit-and-reactivate-the-virtualenv)
      * [8.<span>Create a new DJango project</span>](#8create-a-new-django-project)
         * [1.<span>[code] Use django-admin to create a project</span>](#1code-use-django-admin-to-create-a-project)
         * [<span>After this the folder structure should look like this:</span>](#after-this-the-folder-structure-should-look-like-this)
      * [9.<span>Check the Django project is working</span>](#9check-the-django-project-is-working)
         * [1.<span>[code] </span><span>Change into the project directory which we have created</span>](#1code-change-into-the-project-directory-which-we-have-created)
         * [2.<span>[code] </span><span>Run</span><span> the in temporary server</span>](#2code-runthe-in-temporary-server)
         * [3.<span>Open</span><span> in firefox</span>](#3openin-firefox)
      * [10.<span>Remove the secretkey from settings.py before we intialize first git commit after this section. Store the SecretKey for the time being somewhere</span>](#10remove-the-secretkey-from-settingspy-before-we-intialize-first-git-commit-after-this-section-store-the-secretkey-for-the-time-being-somewhere)
         * [<span>        [code] Edit: settings.py and change to the following and save</span>](#code-edit-settingspy-and-change-to-the-following-and-save)
         * [<span>[image] (Showing settings.py with diff)</span>](#image-showing-settingspy-with-diff)
      * [11.<span>Create git repository and transfer to the github</span>](#11create-git-repository-and-transfer-to-the-github)
         * [1.<span>[code] </span><span>Change into the main project directory</span>](#1code-change-into-the-main-project-directory)
         * [2.<span>[code] Create .gitignore with the following contents</span>](#2code-create-gitignore-with-the-following-contents)
         * [<span>[image] (.gitignore full code)</span>](#image-gitignore-full-code)
         * [<span>Project tree (showing .gitignore)</span>](#project-tree-showing-gitignore)
         * [3.<span>[theory] Git config:</span>](#3theory-git-config)
         * [4.<span>[code] Intialize git repository</span>](#4code-intialize-git-repository)
         * [12.<span>Git steps to commit and push to github</span>](#12git-steps-to-commit-and-push-to-github)
         * [<span>[code] Staging the files: (git add . or git add -A)</span>](#code-staging-the-files-git-add--or-git-add--a)
         * [<span>[code] Check the status</span>](#code-check-the-status)
         * [13.<span>[code] Git</span><span> commit  (dont use git commit -am “message” it will not add new</span><span> files)</span>](#13code-gitcommit-dont-use-git-commit--am-message-it-will-not-add-newfiles)
      * [14.<span>Transfer to the github use sshkeys</span>](#14transfer-to-the-github-use-sshkeys)
         * [1.<span>[code] </span><span>Generate an ssh-key and passphrase in the system using</span>](#1code-generate-an-ssh-key-and-passphrase-in-the-system-using)
         * [2.<span>[code] </span><span>view the ssh key</span>](#2code-view-the-ssh-key)
         * [3.<span>[code] Copy the ssh key into github</span>](#3code-copy-the-ssh-key-into-github)
         * [4.<span>[code] Check the ssh connection</span>](#4code-check-the-ssh-connection)
         * [5.<span>[code] Get the ssh url from github.</span>](#5code-get-the-ssh-url-from-github)
         * [6.<span>[code] Add the ssh url to remote in git</span>](#6code-add-the-ssh-url-to-remote-in-git)
         * [7.<span>[code] Verify </span><span>remote</span><span> urls</span>](#7code-verify-remoteurls)
         * [8.<span>[code]  </span><span>Reset the remote url , if one has added multiple remote urls (not required if there is only one remote url in git remote -v</span>](#8code-reset-the-remote-url--if-one-has-added-multiple-remote-urls-not-required-if-there-is-only-one-remote-url-in-git-remote--v)
      * [15.<span>Git push</span>](#15git-push)
         * [9.<span>[code] First time git push with setting up the --set-upstream (-u) and which branch</span>](#9code-first-time-git-push-with-setting-up-the---set-upstream--u-and-which-branch)
      * [<span>[Git clone: Sometimes we may have to clone back from the github to undo some changes then do</span>](#git-clone-sometimes-we-may-have-to-clone-back-from-the-github-to-undo-some-changes-then-do)
         * [<span>[code]</span>](#code-1)
      * [16.<span>GIT LOG</span>](#16git-log)
         * [<span>[code] </span><span>Commands to view git log and git reflog</span>](#code-commands-to-view-git-log-and-git-reflog)
         * [<span>[code] </span><span>How do I prevent git diff from using a pager?</span>](#code-how-do-i-prevent-git-diff-from-using-a-pager)
   * [<span>FIRST COMMIT END</span>](#first-commit-end)
   * [<span>SECOND COMMIT START</span>](#second-commit-start)
      * [1.<span>Create Postgresql User and Database</span>](#1create-postgresql-user-and-database)
         * [1.<span>[code] Change to root</span>](#1code-change-to-root)
         * [2.<span>[code] </span><span>Change</span><span> to postgres user</span>](#2code-changeto-postgres-user)
         * [3.<span>[code] </span><span>Create</span><span> database user </span>](#3code-createdatabase-user-)
         * [<span>[code] </span><span>Create database with user as owner</span>](#code-create-database-with-user-as-owner)
      * [2.<span>[code] </span><span>Install the PostgreSQL Django adapter, psycopg2</span>](#2code-install-the-postgresql-django-adapter-psycopg2)
      * [3.<span>[theory] Django settings.py for development and production and protect sensitive data</span>](#3theory-django-settingspy-for-development-and-production-and-protect-sensitive-data)
      * [4.<span>[code] </span><span>Install the django-environ in the virtual env</span>](#4code-install-the-django-environ-in-the-virtual-env)
      * [4.<span>Generate random SECRETKEY</span>](#4generate-random-secretkey)
         * [<span>[code] Method 1: cd into the app directory</span>](#code-method-1-cd-into-the-app-directory)
         * [<span>[code] Method 2: from python</span>](#code-method-2-from-python)
      * [5.<span>Setup variables Using .env file in (note .env should be added to .gitignore)</span>](#5setup-variables-using-env-file-in-note-env-should-be-added-to-gitignore)
         * [1.<span>[code] Create a .env file</span>](#1code-create-a-env-file)
         * [2.<span>[code] </span><span>Save</span><span> the .env file in a personal folder outside the project dir. Incase you deleted proj directory you can get back the .env file</span>](#2code-savethe-env-file-in-a-personal-folder-outside-the-project-dir-incase-you-deleted-proj-directory-you-can-get-back-the-env-file)
         * [3.<span>[code] </span><span>Access</span><span> those env variables inside settings.py</span>](#3code-accessthose-env-variables-inside-settingspy)
         * [<span>[code] FULL settings.py file</span>](#code-full-settingspy-file)
         * [<span>Images of settings.py with .env variables</span>](#images-of-settingspy-with-env-variables)
            * [<span>[image] navigation</span>](#image-navigation)
            * [<span>[image] Settings.py full</span>](#image-settingspy-full)
            * [<span>[image] settings.pyf with diff</span>](#image-settingspyf-with-diff)
      * [6.<span>[code] </span><span>Create a .env.example file so that other will know add theirs.</span>](#6code-create-a-envexample-file-so-that-other-will-know-add-theirs)
         * [<span>[image] .env.example file</span>](#image-envexample-file)
      * [<span>        Project tree</span>](#project-tree)
   * [<span>SECOND COMMIT END</span>](#second-commit-end)
   * [<span>THIRD COMMIT START</span>](#third-commit-start)
      * [<span>AIM OF THIRD - Some important tools: install django-extensions,ipython, jupyter, pretty printing dicts or objects by using dir(), runserver_plus and werkzeug, graph models, django_querycount, pudb (debugger), logging, traceback</span>](#aim-of-third---some-important-tools-install-django-extensionsipython-jupyter-pretty-printing-dicts-or-objects-by-using-dir-runserver_plus-and-werkzeug-graph-models-django_querycount-pudb-debugger-logging-traceback)
      * [<span>Pretty printing Objects and SQL with color using json.dumps, sqlparser and pygments, connections, cursor:</span>](#pretty-printing-objects-and-sql-with-color-using-jsondumps-sqlparser-and-pygments-connections-cursor)
         * [<span>[code] Install sqlparse and pygments</span>](#code-install-sqlparse-and-pygments)
         * [<span>[code] Custom functions for pretty pringing</span>](#code-custom-functions-for-pretty-pringing)
         * [<span>[code] Usage in the python shell_plus or jupyter as follows</span>](#code-usage-in-the-python-shell_plus-or-jupyter-as-follows)
         * [<span>[images] Custom pretty functions and its usage</span>](#images-custom-pretty-functions-and-its-usage)
         * [<span>[image] example output of pp_odir(obj)</span>](#image-example-output-of-pp_odirobj)
         * [<span>[image] example of pp_sql_sql(sql), pp_sql_query_pg(user_set), pp_sql_query_any(user_set)</span>](#image-example-of-pp_sql_sqlsql-pp_sql_query_pguser_set-pp_sql_query_anyuser_set)
      * [<span>Install Django-extensions in dev server:</span>](#install-django-extensions-in-dev-server)
         * [<span>[code] installation</span>](#code-installation)
         * [<span>[code] Add into settings.py</span>](#code-add-into-settingspy)
         * [<span>[images] settings.py: adding django_extensions</span>](#images-settingspy-adding-django_extensions)
         * [<span>[code] Some uses of django-extensions</span>](#code-some-uses-of-django-extensions)
      * [<span>Install ipython in dev server:</span>](#install-ipython-in-dev-server)
         * [<span>[code] installation of shell_plus</span>](#code-installation-of-shell_plus)
      * [<span>Install jupyter notebook in dev server:</span>](#install-jupyter-notebook-in-dev-server)
         * [<span>[code] installation of jupyter</span>](#code-installation-of-jupyter)
         * [<span>Modify .gitignore</span>](#modify-gitignore)
         * [<span>[code] How to view formatted sql and dicts in jupyter</span>](#code-how-to-view-formatted-sql-and-dicts-in-jupyter)
      * [<span></span>](#-1)
         * [<span>[code] Some interesting observations in jupyter:</span>](#code-some-interesting-observations-in-jupyter)
      * [<span>Install runserver_plus and werkzeug in dev server:</span>](#install-runserver_plus-and-werkzeug-in-dev-server)
         * [<span>[code] installation of werkzeug</span>](#code-installation-of-werkzeug)
            * [<span>Turn off debugger pin:</span>](#turn-off-debugger-pin)
            * [<span>Never Use with production</span>](#never-use-with-production)
            * [<span>Usage:</span>](#usage)
            * [<span>[image] using of runserver_plus</span>](#image-using-of-runserver_plus)
            * [<span>[theory] how to use</span>](#theory-how-to-use)
      * [<span></span>](#-2)
      * [<span>Install graph_models  and pydotplus to generate UML class diagrams from django models</span>](#install-graph_models-and-pydotplus-to-generate-uml-class-diagrams-from-django-models)
         * [<span>[code] We have already installed django-extensions. So install pydotplus</span>](#code-we-have-already-installed-django-extensions-so-install-pydotplus)
      * [<span>Install django-querycount to know the number of queries:</span>](#install-django-querycount-to-know-the-number-of-queries)
         * [<span>[code] installation and set up</span>](#code-installation-and-set-up)
         * [<span>[code] Customizing the querycount so that it pretty prints the sql</span>](#code-customizing-the-querycount-so-that-it-pretty-prints-the-sql)
         * [<span>[code] Changes to middleware.py</span>](#code-changes-to-middlewarepy)
         * [<span>[image] changes to middleware.py</span>](#image-changes-to-middlewarepy)
         * [<span>[code] Full middleware.py</span>](#code-full-middlewarepy)
         * [<span>[image] full middleware.py</span>](#image-full-middlewarepy)
         * [<span>[code] Add to the settings.py for querycount</span>](#code-add-to-the-settingspy-for-querycount)
         * [<span>[image] add to settings.py querycount customization</span>](#image-add-to-settingspy-querycount-customization)
         * [<span>[image] Example output</span>](#image-example-output)
      * [<span>Pudb: Python debugger</span>](#pudb-python-debugger)
         * [<span>[code] Install pudb and use it</span>](#code-install-pudb-and-use-it)
         * [<span>[image] pudb</span>](#image-pudb)
         * [<span>keybindings</span>](#keybindings)
      * [<span>Logging instead of using printing when level = DEBUG</span>](#logging-instead-of-using-printing-when-level--debug)
         * [<span>[code] Add the following to settings.py. </span>](#code-add-the-following-to-settingspy-)
         * [<span>[theory] The problem with django.db.backends</span>](#theory-the-problem-with-djangodbbackends)
         * [<span>[image] output of logger_custom_string.debug("Any String") will show which line number and the some code around it</span>](#image-output-of-logger_custom_stringdebugany-string-will-show-which-line-number-and-the-some-code-around-it)
         * [<span>[image] settings.py with logging customization</span>](#image-settingspy-with-logging-customization)
      * [<span>Traceback: How to print well formatted traceback at any point in the code</span>](#traceback-how-to-print-well-formatted-traceback-at-any-point-in-the-code)
         * [<span>[code] Add the following code to settings.py</span>](#code-add-the-following-code-to-settingspy)
         * [<span>[image] tracebacl pretty print code</span>](#image-tracebacl-pretty-print-code)
         * [<span>[code] And use it as following</span>](#code-and-use-it-as-following)
      * [<span>Example view to show usage of pretty pritining logging</span>](#example-view-to-show-usage-of-pretty-pritining-logging)
         * [<span>[code] basic_django/views.py</span>](#code-basic_djangoviewspy)
         * [<span>[image] viewps.py</span>](#image-viewpspy)
      * [<span>[code] Settings.py full</span>](#code-settingspy-full)
      * [<span>[image] (full settings.py)</span>](#image-full-settingspy)
      * [<span>[image] (Settings.py Diff)</span>](#image-settingspy-diff)
      * [<span>[code] Creating a view to test logging, dict and trceback with pretty printing</span>](#code-creating-a-view-to-test-logging-dict-and-trceback-with-pretty-printing)
      * [<span>[image] List of Packages installed:</span>](#image-list-of-packages-installed)
   * [<span>THIRD COMMIT END</span>](#third-commit-end)
   * [<span>FOURTH COMMIT START</span>](#fourth-commit-start)
      * [<span>Create an new email without phone verification:</span>](#create-an-new-email-without-phone-verification)
      * [<span>turn on two step verification for this email</span>](#turn-on-two-step-verification-for-this-email)
      * [<span>Create App password:</span>](#create-app-password)
      * [<span>[code] Configure the smtp in Django</span>](#code-configure-the-smtp-in-django)
      * [<span>[image] settings.py email config</span>](#image-settingspy-email-config)
      * [<span>[code] .env file </span>](#code-env-file-)
      * [<span>[image] .env file</span>](#image-env-file)
      * [<span>[code] Change the .env.example</span>](#code-change-the-envexample)
      * [<span>[code] Create a view to send email using send_email()</span>](#code-create-a-view-to-send-email-using-send_email)
      * [<span>[image] basic_django/viewps.py</span>](#image-basic_djangoviewpspy)
      * [<span>[code] Add to the urls.py </span>](#code-add-to-the-urlspy-)
      * [<span>[image] urls.py</span>](#image-urlspy)
      * [<span>Open the url and check</span>](#open-the-url-and-check)
   * [<span>FOURTH COMMIT END</span>](#fourth-commit-end)
   * [<span>FIFTH COMMIT START</span>](#fifth-commit-start)
      * [<span>AIM: CELERY AND REDIS</span>](#aim-celery-and-redis)
      * [<span>[code] Install redis and start redis server</span>](#code-install-redis-and-start-redis-server)
      * [<span>[image] Pipfile</span>](#image-pipfile)
      * [<span>[code] create the file celery.py </span>](#code-create-the-file-celerypy-)
      * [<span>[image] celery.py</span>](#image-celerypy)
      * [<span>[code] <strong>init</strong>.py</span>](#code-initpy)
      * [<span>[image] <strong>init</strong>.py</span>](#image-initpy)
      * [<span>[code] DEFINE TASKS:</span>](#code-define-tasks)
      * [<span>[image] tasks.py</span>](#image-taskspy)
      * [<span>[code] views.py</span>](#code-viewspy)
      * [<span>[image] views.py</span>](#image-viewspy)
      * [<span>[code] FIRST START REDIS</span>](#code-first-start-redis)
      * [<span>[code] START CELERY (go into the project where manage.py is there)</span>](#code-start-celery-go-into-the-project-where-managepy-is-there)
      * [<span>[image] Starting celery</span>](#image-starting-celery)
      * [<span>NOTE: After modify/add tasks refresh celery</span>](#note-after-modifyadd-tasks-refresh-celery)
      * [<span>Flower: Real-time Celery web-monitor</span>](#flower-real-time-celery-web-monitor)
         * [<span>[code] install flower and how to use it</span>](#code-install-flower-and-how-to-use-it)
         * [<span>[image] images</span>](#image-images)
   * [<span>FIFTH COMMIT END</span>](#fifth-commit-end)
   * [<span>SIX COMMIT START</span>](#six-commit-start)
      * [1.<span>Create a custom_user application in Django</span>](#1create-a-custom_user-application-in-django)
         * [<span>[image] directory tree</span>](#image-directory-tree)
   * [<span>SIX COMMIT END</span>](#six-commit-end)
   * [<span>SIX_A COMMIT START</span>](#six_a-commit-start)
      * [<span>Add custom_user to INSTALLED_APPS  of settings.py</span>](#add-custom_user-to-installed_apps-of-settingspy)
      * [<span>        [image] settings.py diff</span>](#image-settingspy-diff)
   * [<span>SIX_A COMMIT END</span>](#six_a-commit-end)
   * [<span>SEVENTH COMMIT THEORY START</span>](#seventh-commit-theory-start)
      * [<span>Custom User model</span>](#custom-user-model)
         * [<span>CONCEPTS TO BE UNDERSTOOD BEFORE STARTING WITH CREATING CUSTOM USER MODEL</span>](#concepts-to-be-understood-before-starting-with-creating-custom-user-model)
            * [1.<span>AUTH_USER_MODEL</span>](#1auth_user_model)
            * [2.<span>Custom model extending </span><span>AbstractUser</span>](#2custom-model-extending-abstractuser)
            * [3.<span>Also</span><span>, register the model in the app’s </span><span>admin.py</span><span>:</span>](#3also-register-the-model-in-the-apps-adminpy)
            * [4.<span>Model Manager:</span>](#4model-manager)
            * [5.<span>Manager names</span>](#5manager-names)
            * [6.<span>Custom managers</span>](#6custom-managers)
            * [7.<span>Custom User fields (</span><span>USERNAME_FIELD, EMAIL_FIELD</span><span>, </span><span>REQUIRED_FIELDS</span><span>)</span>](#7custom-user-fields-username_field-email_field-required_fields)
            * [<span>Abstract Base Classes</span>](#abstract-base-classes)
            * [<span></span>](#-1)
            * [8.<span>Underscore Prefix</span>](#8underscore-prefix)
   * [<span>SEVENTH COMMIT THEORY END</span>](#seventh-commit-theory-end)
   * [<span>EIGHT COMMIT START</span>](#eight-commit-start)
      * [<span>AIM OF SIXTH COMMIT - FLowchart for User Auth - Session based</span>](#aim-of-sixth-commit---flowchart-for-user-auth---session-based)
      * [<span>Logic:</span>](#logic)
         * [<span>Login Page FLow Chart:</span>](#login-page-flow-chart)
         * [<span>Create new User and Pass Page Flow Chart:</span>](#create-new-user-and-pass-page-flow-chart)
         * [<span>Otp page for login_via_otp:</span>](#otp-page-for-login_via_otp)
         * [<span>Reset password:</span>](#reset-password)
      * [<span></span>](#-2)
      * [<span>Making flowcharts using libreoffice draw:</span>](#making-flowcharts-using-libreoffice-draw)
   * [<span>EIGHT COMMIT END</span>](#eight-commit-end)
   * [<span>NINTH COMMIT START</span>](#ninth-commit-start)
      * [<span>[theory] </span><span>Creating Custom user with email as login:</span>](#theory-creating-custom-user-with-email-as-login)
      * [<span>[code] </span><span>Custom user fields:</span>](#code-custom-user-fields)
      * [<span>[image] showing the fields of custom_user</span>](#image-showing-the-fields-of-custom_user)
      * [<span>Usersessions Log</span>](#usersessions-log)
      * [<span>[code] list of things to store for every user session</span>](#code-list-of-things-to-store-for-every-user-session)
         * [<span>[code] Ip_address and settings.py:</span>](#code-ip_address-and-settingspy)
         * [<span>[image] ip_address</span>](#image-ip_address)
      * [<span>[image] showing the Usersessionlog</span>](#image-showing-the-usersessionlog)
      * [<span>[code] models.py  Full code</span>](#code-modelspy-full-code)
      * [<span>[image] models.py (full code)</span>](#image-modelspy-full-code)
      * [<span>[code] Integrate custom_user with admin module</span>](#code-integrate-custom_user-with-admin-module)
      * [<span>[image] admin.py</span>](#image-adminpy)
      * [<span>[code]</span><span>Change in Settings</span>](#codechange-in-settings)
      * [<span>[image] settings.py</span>](#image-settingspy)
      * [1.<span>RUNNING MIGRATION FOR FIRST TIME</span>](#1running-migration-for-first-time)
      * [<span>[code] migrate with sql commands executed</span>](#code-migrate-with-sql-commands-executed)
      * [<span>[image] makemigrationa and migrate</span>](#image-makemigrationa-and-migrate)
      * [<span>[image] migrate output with sql</span>](#image-migrate-output-with-sql)
      * [<span>[image]                         </span><span>Look at the table created after migration in postgresql:</span>](#image-look-at-the-table-created-after-migration-in-postgresql)
      * [<span>Initialize the ActionTypeForUserSessionLog Table</span>](#initialize-the-actiontypeforusersessionlog-table)
         * [<span>[code] ActionTypeForUserSessionLog.json</span>](#code-actiontypeforusersessionlogjson)
         * [<span>[code] insert</span>](#code-insert)
   * [<span>NINTH</span><span> COMMIT END</span>](#ninthcommit-end)
   * [<span>TENTH COMMIT START</span>](#tenth-commit-start)
      * [<span>Philosophy behind admin page</span>](#philosophy-behind-admin-page)
      * [<span>Creating an admin user¶</span>](#creating-an-admin-user)
      * [<span>Start the development server</span>](#start-the-development-server)
      * [<span>How to reset Django admin password?</span>](#how-to-reset-django-admin-password)
      * [<span>If admin login does not work</span>](#if-admin-login-does-not-work)
   * [<span>TENTH</span><span> COMMIT END</span>](#tenthcommit-end)
   * [<span>ELEVENTH COMMIT START</span>](#eleventh-commit-start)
      * [<span>Create an app called login_register_password and articles  </span>](#create-an-app-called-login_register_password-and-articles-)
         * [<span>[image] Directory tree (sorted w.r.t time desc) after startapp</span>](#image-directory-tree-sorted-wrt-time-desc-after-startapp)
   * [<span>ELEVENTH COMMIT END</span>](#eleventh-commit-end)
   * [<span>ELEVENTH_A COMMIT START</span>](#eleventh_a-commit-start)
         * [<span>[image]</span>](#image)
   * [<span>ELEVENTH_A COMMIT END</span>](#eleventh_a-commit-end)
   * [<span>TWELVETH </span><span>COMMIT START</span>](#twelveth-commit-start)
      * [<span>Aim: To create a login via email and OTP. </span>](#aim-to-create-a-login-via-email-and-otp-)
         * [<span>[image] Home Page</span>](#image-home-page)
         * [<span>[image] Email form</span>](#image-email-form)
         * [<span>[image] OTP form</span>](#image-otp-form)
         * [<span>[image] Login confirmation and back to home page</span>](#image-login-confirmation-and-back-to-home-page)
         * [<span>[image] Logout confirmation and back to home page</span>](#image-logout-confirmation-and-back-to-home-page)
      * [<span>Install pyjwt</span>](#install-pyjwt)
         * [<span>[code]</span>](#code)
         * [<span>[image]</span>](#image-1)
      * [<span>Templates and Static files structure:</span>](#templates-and-static-files-structure)
         * [<span>[image] template and static folders for login_register_password and articles</span>](#image-template-and-static-folders-for-login_register_password-and-articles)
      * [<span>MESSAGES For Templates:</span>](#messages-for-templates)
         * [<span>[image]</span>](#image-2)
         * [<span>Using: And then in views.py call</span>](#using-and-then-in-viewspy-call)
         * [<span>Clearing all messages</span>](#clearing-all-messages)
      * [<span>TEMPLATES FOR login_register_password</span>](#templates-for-login_register_password)
         * [<span>base.html</span>](#basehtml)
         * [<span>[image]</span>](#image-3)
         * [<span>login_via_otp/user_login_via_otp_form_email.html</span>](#login_via_otpuser_login_via_otp_form_emailhtml)
         * [<span>[image]</span>](#image-4)
         * [<span>login_via_otp/user_login_via_otp_form_otp.html</span>](#login_via_otpuser_login_via_otp_form_otphtml)
         * [<span>[image]</span>](#image-5)
         * [<span>login_via_otp/email/login_otp_sendemail.html</span>](#login_via_otpemaillogin_otp_sendemailhtml)
         * [<span>[image]</span>](#image-6)
      * [<span>TEMPLATES FOR articles</span>](#templates-for-articles)
         * [<span>base.html</span>](#basehtml-1)
         * [<span>[image]</span>](#image-7)
         * [<span>main_page/articles.html</span>](#main_pagearticleshtml)
         * [<span>[image]</span>](#image-8)
      * [<span>Urls</span>](#urls)
      * [<span>Urls of Articles</span>](#urls-of-articles)
         * [<span>Urls.py</span>](#urlspy)
         * [<span>[image]</span>](#image-9)
      * [<span>Urls of login_register_password</span>](#urls-of-login_register_password)
         * [<span>Urls.py</span>](#urlspy-1)
         * [<span>[image]</span>](#image-10)
      * [<span>Urls of basic_django</span>](#urls-of-basic_django)
         * [<span>Urls.py</span>](#urlspy-2)
         * [<span>[image]</span>](#image-11)
         * [<span>[image] diff</span>](#image-diff)
      * [<span>Forms: login_register_password</span>](#forms-login_register_password)
         * [<span>Forms.py</span>](#formspy)
         * [<span>[image] (mainly for file location view)</span>](#image-mainly-for-file-location-view)
         * [<span>[image] forms.py code</span>](#image-formspy-code)
      * [<span>Views.py of login_register_password</span>](#viewspy-of-login_register_password)
         * [<span>Views.py</span>](#viewspy)
         * [<span>[image] [file location view]</span>](#image-file-location-view)
         * [<span>[image] code view</span>](#image-code-view)
         * [<span>Views of articles.py</span>](#views-of-articlespy)
         * [<span>Views.py</span>](#viewspy-1)
         * [<span>[image] code</span>](#image-code)
      * [<span>Celery tasks for sending emails:</span>](#celery-tasks-for-sending-emails)
         * [<span>[code]</span>](#code-1)
      * [<span>Request.SESSION: for passing making data available to next view.</span>](#requestsession-for-passing-making-data-available-to-next-view)
      * [<span>PYTHON: RuntimeWarning: DateTimeField received a naive datetime while time zone support is active. RuntimeWarning)</span>](#python-runtimewarning-datetimefield-received-a-naive-datetime-while-time-zone-support-is-active-runtimewarning)
      * [<span>Form &gt; View &gt; html</span>](#form--view--html)
      * [<span>Create a Form for login via OTP</span>](#create-a-form-for-login-via-otp)
   * [<span>TWELVETH COMMIT END</span>](#twelveth-commit-end)
   * [<span>MISCELLENEOUS</span>](#miscelleneous)
      * [<span>Q: using model.save() from django shell will not validate the data</span>](#q-using-modelsave-from-django-shell-will-not-validate-the-data)
      * [<span>Tip: Log SQL Queries To Console</span>](#tip-log-sql-queries-to-console)
         * [<span>Option 1: Django-debug-toolbar</span>](#option-1-django-debug-toolbar)
            * [<span>*** Drawback: </span>](#-drawback-)
         * [<span>Option 2: django-extensions</span>](#option-2-django-extensions)
         * [<span>*** Print sql queries in jupyter notebook with django-extensions plugin</span>](#-print-sql-queries-in-jupyter-notebook-with-django-extensions-plugin)
         * [<span>Option 3: django-querycount</span>](#option-3-django-querycount)
         * [<span>Option 4: Django logging</span>](#option-4-django-logging)
            * [<span>Advantage: </span>](#advantage-)
         * [<span>Option 4mod: Django logging when we want</span>](#option-4mod-django-logging-when-we-want)
         * [<span>Option 5: django-print-sql</span>](#option-5-django-print-sql)
         * [<span>Option 6: sql log</span>](#option-6-sql-log)
      * [<span>Understanding logging in Python:</span>](#understanding-logging-in-python)
         * [<span>print is not a good idea</span>](#print-is-not-a-good-idea)
         * [<span>Use Python standard logging module</span>](#use-python-standard-logging-module)
         * [<span>PYTHON LOGGING LEVELS</span>](#python-logging-levels)
         * [<span>There are 4 main concepts in Python logging:</span>](#there-are-4-main-concepts-in-python-logging)
         * [<span>Example - Configuring logging</span>](#example---configuring-logging)
         * [<span>PYTHON LOGGING HANDLER</span>](#python-logging-handler)
         * [<span>PYTHON LOGGER</span>](#python-logger)
         * [<span>A logger has three main fields:</span>](#a-logger-has-three-main-fields)
         * [<span>A logger is unique by name,</span>](#a-logger-is-unique-by-name)
         * [<span>Root logger</span>](#root-logger)
         * [<span>Parent logger (a.b)</span>](#parent-logger-ab)
         * [<span>Logger hierarchy</span>](#logger-hierarchy)
         * [<span>Effective logger level w.r.t NOTSET and w.r.t parent is root or not</span>](#effective-logger-level-wrt-notset-and-wrt-parent-is-root-or-not)
         * [<span>NOTSET level and Log Level vs logger level</span>](#notset-level-and-log-level-vs-logger-level)
         * [<span>use <strong>name</strong> as the logger name: </span>](#use-name-as-the-logger-name-)
      * [<span>How to show queries log in PostgreSQL?</span>](#how-to-show-queries-log-in-postgresql)
      * [<span>Django: </span><span>Database access optimization:</span>](#django-database-access-optimization)
      * [<span>QuerySets are lazy</span>](#querysets-are-lazy)
      * [<span>When QuerySets are evaluated</span>](#when-querysets-are-evaluated)
      * [<span>Logging and propogate:</span>](#logging-and-propogate)
      * [<span>Logging and query sets are Lazy:</span>](#logging-and-query-sets-are-lazy)
      * [<span>Logging and jupyter notebook and Lazy_load:</span>](#logging-and-jupyter-notebook-and-lazy_load)
      * [<span>How to pretty print a class object and ignore typeerror only for dispalying: json.dumps and default=str</span>](#how-to-pretty-print-a-class-object-and-ignore-typeerror-only-for-dispalying-jsondumps-and-defaultstr)
      * [<span>dir() does much more than look up <strong>dict</strong></span>](#dir-does-much-more-than-look-up-dict)
      * [<span>Python dictionary key error when assigning - how do I get around this?</span>](#python-dictionary-key-error-when-assigning---how-do-i-get-around-this)
      * [<span>How to add dictionary items to list in python:</span>](#how-to-add-dictionary-items-to-list-in-python)
      * [<span>How to get the properties of an object:</span>](#how-to-get-the-properties-of-an-object)
      * [<span>What are metaclasses in Python?</span>](#what-are-metaclasses-in-python)
      * [<span>Getting the sql of a query in  jupyter</span>](#getting-the-sql-of-a-query-in-jupyter)
         * [<span>1) using mogrify from Psycopg extension</span>](#1-using-mogrify-from-psycopg-extension)
         * [<span>2) Executing a new sql with EXPLAIN using cursor and then get the sql</span>](#2-executing-a-new-sql-with-explain-using-cursor-and-then-get-the-sql)
         * [<span>3) Using connections[‘default’].queries</span>](#3-using-connectionsdefaultqueries)
      * [<span>defaultdict() : assign default value when key does not exist</span>](#defaultdict--assign-default-value-when-key-does-not-exist)
      * [<span>counter(): collections — High-performance container datatypes</span>](#counter-collections--high-performance-container-datatypes)
      * [<span>Python Concatenation (string   variables)</span>](#python-concatenation-string--variables)
      * [<span>How to get the project from git and start fresh</span>](#how-to-get-the-project-from-git-and-start-fresh)
      * [<span>introspect properties and model fields in Django?</span>](#introspect-properties-and-model-fields-in-django)
      * [<span>Django render a template</span>](#django-render-a-template)
         * [<span>A shortcut: render()</span>](#a-shortcut-render)
         * [<span>Raising a 404 error¶</span>](#raising-a-404-error)
         * [<span>A shortcut: get_object_or_404()¶</span>](#a-shortcut-get_object_or_404)
         * [<span>Philosophy</span>](#philosophy)
      * [<span>Passing variables between views:</span>](#passing-variables-between-views)
      * [<span>Want to check if a key is set in session</span>](#want-to-check-if-a-key-is-set-in-session)
      * [<span>Using redirect() to redirect to another view</span>](#using-redirect-to-redirect-to-another-view)
      * [<span>URL Namespace</span>](#url-namespace)
      * [<span>Messages Django:</span>](#messages-django)
      * [<span>os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'basic_django.settings') - will not modify/create new shell Env variables.</span>](#osenvironsetdefaultdjango_settings_module-basic_djangosettings---will-not-modifycreate-new-shell-env-variables)
      * [<span>Python Relative and Absolute Import</span>](#python-relative-and-absolute-import)
      * [<span>Decorators Python</span>](#decorators-python)
      * [<span>Celery and Redis</span>](#celery-and-redis)
         * [<span>For Django</span>](#for-django)
         * [<span>Shared_task vs task</span>](#shared_task-vs-task)
      * [<span>Flower: Real-time Celery web-monitor</span>](#flower-real-time-celery-web-monitor)
      * [<span>Django Authentication:</span>](#django-authentication)
      * [<span>How to log a user in</span>](#how-to-log-a-user-in)
      * [<span>How to log a user out¶</span>](#how-to-log-a-user-out)
      * [<span>Retrieving all field instances of a model (_meta)</span>](#retrieving-all-field-instances-of-a-model-_meta)
      * [<span>Django's Built in Authentication</span>](#djangos-built-in-authentication)
      * [<span>Application Configuration feature someapp.apps.AppConfig</span>](#application-configuration-feature-someappappsappconfig)
      * [<span>DJANGO SECRET_KEY:</span>](#django-secret_key)
      * [<span>Why dont we see the session variable in the chrome:</span>](#why-dont-we-see-the-session-variable-in-the-chrome)
      * [<span>In the template user is available </span>](#in-the-template-user-is-available-)
      * [<span>What is need to login a user</span>](#what-is-need-to-login-a-user)
      * [<span>Django - allow url only to be accessed from a specific page</span>](#django---allow-url-only-to-be-accessed-from-a-specific-page)
      * [<span>Logging does not work in try: except: </span>](#logging-does-not-work-in-try-except-)
      * [<span>if key in dict vs. try/except - which is more readable idiom?</span>](#if-key-in-dict-vs-tryexcept---which-is-more-readable-idiom)
      * [<span>Datetime using timezone when passing data using session or json</span>](#datetime-using-timezone-when-passing-data-using-session-or-json)
      * [<span>Convert datetime string to python datetime</span>](#convert-datetime-string-to-python-datetime)
      * [<span>Comparing timestamp and difference</span>](#comparing-timestamp-and-difference)
      * [<span>How to store information of user_login ip_address, device, and multiple logins information</span>](#how-to-store-information-of-user_login-ip_address-device-and-multiple-logins-information)
      * [<span>How to get client ip address in Django</span>](#how-to-get-client-ip-address-in-django)
      * [<span>Models on_delete</span>](#models-on_delete)
      * [<span>Role of get_user:</span>](#role-of-get_user)
      * [<span>How the authentication works in Django</span>](#how-the-authentication-works-in-django)
      * [<span>Django model object.create vs object.save</span>](#django-model-objectcreate-vs-objectsave)
      * [<span>Retrieving all field instances of a model</span>](#retrieving-all-field-instances-of-a-model)
      * [<span>Sort User dictionary for viewing</span>](#sort-user-dictionary-for-viewing)
      * [<span>View all fields (including hidden) with only certain fields:</span>](#view-all-fields-including-hidden-with-only-certain-fields)
         * [<span>[image] run this script in jupyter</span>](#image-run-this-script-in-jupyter)
         * [<span>[image] Output</span>](#image-output)
      * [<span>auto_now/auto_now_add will not update with .update</span>](#auto_nowauto_now_add-will-not-update-with-update)
      * [<span>Django form editable</span>](#django-form-editable)
      * [<span>Django set_password and password validators and password changed</span>](#django-set_password-and-password-validators-and-password-changed)
      * [<span>Specifying which fields to save by update_fields rather than saving the whole fields again.</span>](#specifying-which-fields-to-save-by-update_fields-rather-than-saving-the-whole-fields-again)
      * [<span>How Django knows to UPDATE vs. INSERT¶</span>](#how-django-knows-to-update-vs-insert)
      * [<span>Django Charfield null=False Integrity Error not raised</span>](#django-charfield-nullfalse-integrity-error-not-raised)
      * [<span>Raise a validation error in a model's save method in Django</span>](#raise-a-validation-error-in-a-models-save-method-in-django)
      * [<span>Difference between super() and super (className,self) in Python [duplicate]</span>](#difference-between-super-and-super-classnameself-in-python-duplicate)
      * [<span>Sublime Text expand Selection to indentation</span>](#sublime-text-expand-selection-to-indentation)
      * [<span>Sublime Text folding</span>](#sublime-text-folding)
      * [<span>User.save(update_fields=[‘last_login’])</span>](#usersaveupdate_fieldslast_login)
      * [<span>Delete a object</span>](#delete-a-object)
      * [<span>logout() and maximum recursion depth exceeded on logout(request)</span>](#logout-and-maximum-recursion-depth-exceeded-on-logoutrequest)
      * [<span>Model.objects.get() (should return only one object)</span>](#modelobjectsget-should-return-only-one-object)
      * [<span>Git insert commit inbetween</span>](#git-insert-commit-inbetween)
      * [<span>How to revert initial git commit?</span>](#how-to-revert-initial-git-commit)
      * [<span>Recursively removes all .pyc files and <strong>pycache</strong> directories in the current directory</span>](#recursively-removes-all-pyc-files-and-pycache-directories-in-the-current-directory)
      * [<span>Git how to revert back to the last commit by cleaning the working directory</span>](#git-how-to-revert-back-to-the-last-commit-by-cleaning-the-working-directory)
      * [<span>Git ammed without opening the editor</span>](#git-ammed-without-opening-the-editor)
      * [<span>ffmpeg : how to record a gif:</span>](#ffmpeg--how-to-record-a-gif)
      * [<span>Git how to use rebase --onto</span>](#git-how-to-use-rebase---onto)
         * [<span>Git rebase (two argument form)</span>](#git-rebase-two-argument-form)
         * [<span>Git rebase (another explanation)</span>](#git-rebase-another-explanation)
      * [<span>Insert a commit before the root commit in Git?</span>](#insert-a-commit-before-the-root-commit-in-git)
      * [<span>Ammed the latest git commit message if its empty git</span>](#ammed-the-latest-git-commit-message-if-its-empty-git)
      * [<span>How to make Git “forget” about a file that was tracked but is now in .gitignore?</span>](#how-to-make-git-forget-about-a-file-that-was-tracked-but-is-now-in-gitignore)
      * [<span>How to insert a commit inbetween</span>](#how-to-insert-a-commit-inbetween)
* # Basic Django Setup Documentation:

* # GOAL OF THIS PROJECT:

 * ## Session based Login using email and OTP and covering the basic django setup required

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>To create a small home page, with login/logout link<br><br>Any one can login with an email id. OTP will be sent to their email id. If Correct OTP is entered before it gets expired then one is logged in and will be returned back to home page<br></td></tr></tbody></table>

     * The below images will shows the urls and the flow

     * ### \[image\] Home Page

       * ![](images/image72.png)

       * Now one wants to login (may be to comment etc) will click on login

     * ### \[image\] Email form

       * ![](images/image103.png)

     * ### \[image\] OTP form

       * ![](images/image44.png)

     * ### \[image\] Login confirmation and back to home page

       * ![](images/image102.png)

       * One wants to logout, He will click logout

     * ### \[image\] Logout confirmation and back to home page

       * ![](images/image147.png)

* # DOCUMENTATION START

     * I tried to keep the commits in the order of the documentation of the coding. So that its easy to know whats happening or how things are done. 

     * We use git and with the help of rebase we all ways try to keep all the documentation content only in the first commit. This will help in visualizing the main program files nicely. One of the goals is also the see progressively all file changes. I use \[ gitk --all \] to see the commits nicely.

     * Lot of effort was put to make a full document. Even we dont have the project files, one should be able to build back the project from scratch.

* # NEVER DO FIRST MIGRATION WITHOUT CREATING A CUSTOM “USER” MODEL and setting AUTH\_USER\_MODEL = custom\_user.User in Settings.py

     * In django we generall do migration after creating a django project and configuring the database in settings.py. Also ./manage.py runserver  shows warning that migrations are pending. Basically there are many applications which are mentioned in INSTALLED APPS which need to setup their tables in database.

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>$ python manage.py makemigrations<br>$ python manage.py migrate<br></td></tr></tbody></table>

     * So Never do this before creating a custom\_user in the below document, else later when we want to create a custom user we empty database and do fresh from start.

* # NEVER UPGRADE POSTGRESQL WITHOUT TAKING BACKUP. 

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td><ul><li>From version 10.0 onwards PostgreSQL <a href="https://www.google.com/url?q=https://www.postgresql.org/about/news/1786/&amp;sa=D&amp;ust=1571383143848000" class="c24">changed its versioning scheme</a>. Earlier upgrade from version 9.x to 9.y was considered as major upgrade. Now upgrade from version 10.x to 10.y is considered as minor upgrade and upgrade from version 10.x to 11.y is considered as major upgrade.</li></ul></td></tr></tbody></table>

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>It is recommended to add the following to your /etc/pacman.conf file:<br>IgnorePkg = postgresql postgresql-libs<br>This will ensure you do not accidentally upgrade the database to an incompatible version. When an upgrade is available, pacman will notify you that it is skipping the upgrade because of the entry in pacman.conf. Minor version upgrades are safe to perform. However, if you do an accidental upgrade to a different major version, you might not be able to access any of your data<br></td></tr></tbody></table>

* # TAKING BACKUP OF ENTIRE POSTGRESQL DATABASES

     * To support convenient dumping of the entire contents of a database cluster, the [pg\_dumpall](https://www.google.com/url?q=https://www.postgresql.org/docs/current/app-pg-dumpall.html&sa=D&ust=1571383143852000) program is provided. pg\_dumpall backs up each database in a given cluster, and also preserves cluster-wide data such as role and tablespace definitions. The basic usage of this command is:

     * The resulting dump can be restored with psql:

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>#gauranga<br>psql -f dumpfile postgres<br></td></tr></tbody></table>

     * (Actually, you can specify any existing database name to start from, but if you are loading into an empty cluster then postgres should usually be used.) It is always necessary to have database superuser access when restoring a pg\_dumpall dump, as that is required to restore the role and tablespace information. If you use tablespaces, make sure that the tablespace paths in the dump are appropriate for the new installation.

* # README MAKING for Github Documentation using google doc to MarkDown:

     * AIM: I want to document nicely all my code. So after lot of R\&D i found an easy way using google doc, pandoc, gh-md-toc and grip. The below will show in detail:

     * 1.  Create a google doc. 

     * Google doc provides the facility to online create word documents. 

     * - Use Heading 1, Heading 2 etc so that it will converted to Headings in markdown also

     * - Use tables to show code

     * - You can add images from computer. Dont put images from online. Or first save them to comp

     * 2.  Save the google doc as html, zip 

     * 3.  Unzip the contents into folder

     * - You will find a html file and an images folder

     * 4.  In linux we use pandoc command to convert html to markdown format

 * ## \[code\] Follow the below steps to convert to README.md with TOC and indenting

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>$ htmlinput="DjangoDocumentation.html"; mdoutput="DjangoDocumentation.md";  mdfinal="README.md"<br>pandoc -f html -t gfm --wrap=preserve -o $mdoutput $htmlinput<br>sed -i -r "s/^([0-9]+\.)( +#+ +)/\2\1/g" $mdoutput <br>sed -i -r "s/^ +//g" $mdoutput<br>sed -i -r 's/&lt;!-- end list --&gt;//g' $mdoutput<br>cp /home/web_dev/github_personl_token_for_gh_md_toc/token.txt .<br>split -b 300KB $mdoutput<br>rm -rf toc<br>mkdir toc<br>for f in x*;  <br>do <br>cat $f | gh-md-toc - &gt; toc/$f.toc <br>done;<br>cat toc/*.toc &gt; toc.md<br>sed -i -r 's/&lt;span[^&gt;]*&gt;//g' $mdoutput<br>sed -i -r 's/&lt;\/span&gt;//g' $mdoutput<br>sed -i -r 's/&lt;p[^&gt;]*&gt;//g' $mdoutput<br>sed -i -r 's/&lt;\/p&gt;/&lt;br&gt;/g' $mdoutput<br>awk '/&lt;table&gt;/{ORS=""} /&lt;\/table&gt;/{ORS=RS} 1' $mdoutput &gt; tmp &amp;&amp; mv tmp $mdoutput<br>sed -i '/^$/d;G' $mdoutput<br>sed -i -r 's/^./     * &amp;/' $mdoutput<br>sed -i -r 's/^     \* (#[^#])/* \1/g' $mdoutput<br>sed -i -r 's/^     \* (##[^#])/ * \1/g' $mdoutput<br>sed -i -r 's/^     \* (###[^#])/     * \1/g' $mdoutput<br>sed -i -r 's/^     \* (####[^#])/       * \1/g' $mdoutput<br>sed -Ez -i 's/(\n)(       )(\* ####[^#][^\n]*\n\n)(     )(\* [^#])/\1\2\3\2  \5/g' $mdoutput<br>sed -Ez -i 's/(\n)(     )(\* ###[^#][^\n]*\n\n)(     )(\* [^#])/\1\2\3\2  \5/g' $mdoutput<br>sed -Ez -i 's/(\n)( )(\* ###[^#][^\n]*\n\n)(     )(\* [^#])/\1\2\3\2    \5/g' $mdoutput<br>sed -Ez -i 's/(\n)(\* ###[^#][^\n]*\n\n)(     )(\* [^#])/\1\2\3 \4/g' $mdoutput<br>awk 'BEGIN{count=0; prevNR=0; prevChar=""} match($0,/^(( +)(\*)( +))([^#].*)/,a){if(prevNR!=0 &amp;&amp; NR == prevNR+2){print prevChar a[5]; prevNR = NR; } else{print; prevChar = a[1]; prevNR = NR} } !/^(( +)(\*)( +))([^#].*)/{ print } /^ +\* +#/{ prevChar = "" } ' $mdoutput &gt; tmp &amp;&amp; mv tmp $mdoutput<br>cat toc.md $mdoutput &gt; $mdfinal<br><br>************ EXPLANATION of the above steps **************<br>Note: <a href="https://www.google.com/url?q=https://explainshell.com/&amp;sa=D&amp;ust=1571383143864000" class="c24">https://explainshell.com/</a> (helps to understand shell commands)<br><br>Step 1: Download google doc's file as html,zipped and unzip in a folder<br><br>Step : Store input and output filenames as linux variables so that its easy to make is generic<br><br>htmlinput="DjangoDocumentation.html"; mdoutput="DjangoDocumentation.md";  mdfinal="README.md"<br><br>Step 2: Convert html to markdown using pandoc <br>pandoc -f html -t gfm --wrap=preserve -o $mdoutput $htmlinput<br><br>--gfm GitHub Flavored Markdown<br><br>Step 3: move number after the hash<br>sed -i -r "s/^([0-9]+\.)( +#+ +)/\2\1/g" $mdoutput<br><br>i[SUFFIX], --in-place[=SUFFIX]<br>      edit files in place (makes backup if extension supplied)<br>-r, --regexp-extended<br>       use extended regular expressions in the script.<br><br>The s command (as in substitute) is probably the most important in sed and has a lot of different options. The syntax of the s command is ‘s/regexp/replacement/flags’.<br><br><a href="https://www.google.com/url?q=https://www.geeksforgeeks.org/sed-command-in-linux-unix-with-examples/&amp;sa=D&amp;ust=1571383143869000" class="c24">https://www.geeksforgeeks.org/sed-command-in-linux-unix-with-examples/</a><br>$sed '1,3 s/unix/linux/g' geekfile.txt  (replace lines between 1 and 3)<br>$sed '3,6d' filename.txt (delete range of lines)<br>sed '/pattern/d' filename.txt (delete pattern matching line)<br><br>\2\1 represents the () group patterns<br><br>Prev: (number if before #)<br>1.  # &lt;span class="c41 c39"&gt;NEVER DO FIRST MIGRATION WITHOUT CREATING A CUSTOM <br><br>After: (number after #)<br>  # 1.&lt;span class="c41 c39"&gt;NEVER DO FIRST MIGRATION WITHOUT CREATING A CUSTOM<br><br>Step 4: remove empty spaces in the beginning of the line<br>sed -i -r "s/^ +//g" DjangoDocumentaion.md <br><br>Prev: (space in the beginning of line)<br>  # 1.&lt;span class="c41 c39"&gt;NEVER DO FIRST MIGRATION WITHOUT CREATING A CUSTOM<br><br>After: (removed space in the beginning of line)<br># 1.&lt;span class="c41 c39"&gt;NEVER DO FIRST MIGRATION WITHOUT CREATING A CUSTOM <br><br>Step 5: remove &lt;!-- end list --&gt;<br>sed -i -r 's/&lt;!-- end list --&gt;//g' DjangoDocumentaion.md<br><br>Step 6: Create TOC using gh-md-toc. Download using <br>wget https://raw.githubusercontent.com/ekalinin/github-markdown-toc/master/gh-md-toc <br>and then chmod +x  gh-md-toc and then cp to /usr/bin/ folder <br><br>Step 6.a: Create toc and save them in toc.md<br>1) Github api has some limitations. We cant use a file more than 400kb so we have to split the file before we send<br>2) to use github api: with OAuth 5000/hour and without 60/hour<br><br>Creating a token<br><br>Verify your email address, if it hasn't been verified yet.<br><br>In the upper-right corner of any page, click your profile photo, then click Settings.<br><br>Settings icon in the user bar<br>In the left sidebar, click Developer settings.<br><br>Developer settings<br>In the left sidebar, click Personal access tokens.<br><br>Personal access tokens<br>Click Generate new token.<br><br>Generate new token button<br>Give your token a descriptive name.<br><br>Token description field<br>Select the scopes, or permissions, you'd like to grant this token. To use your token to access repositories from the command line, select repo. We select user scope for using gh-md-toc<br><br>Selecting token scopes<br>Click Generate token.<br><br>Generate token button<br>Click  to copy the token to your clipboard. For security reasons, after you navigate off the page, you will not be able to see the token again.<br><br>Once the token is generated store it in a /home/web_dev/github_personl_token_for_gh_md_toc/token.txt<br><br>Eg: echo "2a2dab...563" &gt; /home/web_dev/github_personl_token_for_gh_md_toc/token.txt<br><br># everytime we will copy the token.py to the current directory<br>cp /home/web_dev/github_personl_token_for_gh_md_toc/token.txt .<br><br>#split the file to less than 400kb. This will create files with names xaa, xab etc<br>split -b 300KB $mdoutput<br><br>#creating a directory to store split files. First remove existing dir and then create<br>rm -rf toc<br>mkdir toc<br><br># loop over each split file<br>for f in x*;  <br>do <br># generate toc for each file and store the toc folder<br>cat $f | gh-md-toc - &gt; toc/$f.toc <br>done;<br><br># now combine all the toc files<br>cat toc/*.toc &gt; toc.md<br><br><br>:Note there is a dash after gh-md-toc<br><br>Step 7: Remove &lt;span ..&gt; elements<br>sed -i -r 's/&lt;span[^&gt;]*&gt;//g' DjangoDocumentaion.md<br><br>Step 8: Remove &lt;/span&gt; element<br>sed -i -r 's/&lt;\/span&gt;//g' DjangoDocumentaion.md<br><br>Step 9: Remove &lt;p ...&gt; element<br>sed -i -r 's/&lt;p[^&gt;]*&gt;//g' DjangoDocumentaion.md<br><br>Step 10: Remove &lt;/p&gt;<br>sed -i -r 's/&lt;\/p&gt;/&lt;br&gt;/g' DjangoDocumentaion.md<br><br>Step 11: convert &lt;table&gt;.. multiline ..&lt;/table&gt;  to single line<br>awk '/&lt;table&gt;/{ORS=""} /&lt;\/table&gt;/{ORS=RS} 1' DjangoDocumentaion.md &gt; tmp &amp;&amp; mv tmp DjangoDocumentaion.md<br><br>C-syntax of above awk command<br>While read (filename, line){<br> if ($0 ~ /&lt;table&gt;/){<br>     ORS=""   ---&gt; <br> }<br> if(/&lt;\/table&gt;/){<br>     ORS=RS<br> }<br>}<br><br>It sets ORS=”” when it find &lt;table&gt; and then changes back to RS when it reached &lt;/table&gt;<br><br>Prev:<br>&lt;table&gt;<br>&lt;tbody&gt;<br>&lt;tr&gt;<br>&lt;td&gt;jkhaskjdhkj&lt;/td&gt;<br>&lt;/tr&gt;<br>&lt;/tbody&gt;<br>&lt;/table&gt;<br><br><br>After:<br>&lt;table&gt;&lt;tbody&gt;&lt;tr&gt;&lt;td&gt;jkhaskjdhkj&lt;/td&gt;&lt;/tr&gt;&lt;/tbody&gt;&lt;/table&gt;<br><br><br>Step 12: Remove empty lines and place single balnk line after each line<br>sed -i '/^$/d;G' DjangoDocumentaion.md<br>https://www.geeksforgeeks.org/sed-command-linux-set-2/<br>sed G a.txt (insert one blank line after each line)<br>sed '/love/G' a.txt (Insert a blank line below every line which matches “love”)<br><br>All options of sed <a href="https://www.google.com/url?q=http://www.grymoire.com/Unix/Sed.html&amp;sa=D&amp;ust=1571383143891000" class="c24">http://www.grymoire.com/Unix/Sed.html</a><br><br>Using 'sed -n /pattern/p' to duplicate the function of grep<br>If you want to duplicate the functionality of grep, combine the -n (noprint) option with the /p print flag:<br>http://www.grymoire.com/Unix/Sed.html#uh-15b<br>sed -n '/PATTERN/p' file<br><br>Step 13: Add 5 spaces and * and space in the beginning of each line<br>sed -i -r 's/^./     * &amp;/' DjangoDocumentaion.md <br><br>Step 14: Replace the above with * and space for singel hash<br>sed -i -r 's/^     \* (#[^#])/* \1/g' DjangoDocumentaion.md<br><br>Step 14: Replace the above with space and * and space for singel hash<br>sed -i -r 's/^     \* (##[^#])/ * \1/g' DjangoDocumentaion.md<br><br>Step 14: Replace the above with 5 spaces and * and space for singel hash<br>sed -i -r 's/^     \* (###[^#])/     * \1/g' DjangoDocumentaion.md<br><br>Step 14: Replace the above with 7 spaces and * and space for singel hash<br>sed -i -r 's/^     \* (####[^#])/       * \1/g' DjangoDocumentaion.md<br><br>Step 15<br>awk 'BEGIN{count=0; prevNR=0; prevChar=""} match($0,/^(( +)(\*)( +))([^#].*)/,a){if(prevNR!=0 &amp;&amp; NR == prevNR+2){print prevChar a[5]; prevNR = NR; } else{print; prevChar = a[1]; prevNR = NR} } !/^(( +)(\*)( +))([^#].*)/{ print } /^ +\* +#/{ prevChar = "" } ' DjangoDocumentaion.md &gt; tmp &amp;&amp; mv tmp DjangoDocumentaion.md<br><br>C-syntax <br><br>$ awk 'BEGIN{<br>    count=0;<br>    prevNR=0;<br>    prevChar=""<br>    }<br>    match($0,/^(( +)(\*)( +))([^#].*)/,a){<br>        if(prevNR!=0 &amp;&amp; NR == prevNR+2){<br>            print prevChar a[5]<br>            prevNR = NR<br><br>        }<br>        else{<br>            print;<br>            prevChar = a[1];<br>            prevNR = NR<br>        }<br>    }<br><br>    !/^(( +)(\*)( +))([^#].*)/{<br>        print;<br>    }<br><br>    /^ +\* +#/{<br>            prevChar = "";<br>    }<br><br>    ' testread.md<br><br><br><br>convert :<br><br> * ## 2.Install the PostgreSQL Django adapter, psycopg2<br><br>     * &lt;table&gt;&lt;colgroup&gt;&lt;col style="width: 100%" /&gt;4<br><br>        * &lt;table&gt;&lt;colgroup&gt;&lt;col style="width: 100%" /&gt;&lt;/colgroup&gt;&lt;tbody&gt;1<br><br>    * &lt;table&gt;&lt;colgroup&gt;&lt;col style="width: 100%" /&gt;&lt;/colgroup&gt;&lt;tbody&gt;2<br><br>    * &lt;table&gt;&lt;colgroup&gt;&lt;col style="width: 100%" /&gt;&lt;/colgroup&gt;&lt;tbody&gt;3<br><br>to<br><br> * ## 2.Install the PostgreSQL Django adapter, psycopg2<br><br>     * &lt;table&gt;&lt;colgroup&gt;&lt;col style="width: 100%" /&gt;4<br><br>     * &lt;table&gt;&lt;colgroup&gt;&lt;col style="width: 100%" /&gt;&lt;/colgroup&gt;&lt;tbody&gt;1<br><br>     * &lt;table&gt;&lt;colgroup&gt;&lt;col style="width: 100%" /&gt;&lt;/colgroup&gt;&lt;tbody&gt;2<br><br>     * &lt;table&gt;&lt;colgroup&gt;&lt;col style="width: 100%" /&gt;&lt;/colgroup&gt;&lt;tbody&gt;3<br><br><br>Step 16<br>Append toc.md to the top of the Document and save it as README.md<br>cat toc.md DjangoDocumentaion.md &gt; README.md<br><br>All commands at a time<br><br>$ htmlinput="DjangoDocumentation.html"; mdoutput="DjangoDocumentation.md";  mdfinal="README.md"<br>pandoc -f html -t gfm --wrap=preserve -o $mdoutput $htmlinput<br>sed -i -r "s/^([0-9]+\.)( +#+ +)/\2\1/g" $mdoutput<br>sed -i -r "s/^ +//g" $mdoutput<br>sed -i -r 's/&lt;!-- end list --&gt;//g' $mdoutput<br>cp /home/web_dev/github_personl_token_for_gh_md_toc/token.txt .<br>split -b 300KB $mdoutput<br>rm -rf toc<br>mkdir toc<br>for f in x*;  <br>do <br>cat $f | gh-md-toc - &gt; toc/$f.toc <br>done;<br>cat toc/*.toc &gt; toc.md<br>sed -i -r 's/&lt;span[^&gt;]*&gt;//g' $mdoutput<br>sed -i -r 's/&lt;\/span&gt;//g' $mdoutput<br>sed -i -r 's/&lt;p[^&gt;]*&gt;//g' $mdoutput<br>sed -i -r 's/&lt;\/p&gt;/&lt;br&gt;/g' $mdoutput<br>awk '/&lt;table&gt;/{ORS=""} /&lt;\/table&gt;/{ORS=RS} 1' $mdoutput &gt; tmp &amp;&amp; mv tmp $mdoutput<br>sed -i '/^$/d;G' $mdoutput<br>sed -i -r 's/^./     * &amp;/' $mdoutput<br>sed -i -r 's/^     \* (#[^#])/* \1/g' $mdoutput<br>sed -i -r 's/^     \* (##[^#])/ * \1/g' $mdoutput<br>sed -i -r 's/^     \* (###[^#])/     * \1/g' $mdoutput<br>sed -i -r 's/^     \* (####[^#])/       * \1/g' $mdoutput<br>sed -Ez -i 's/(\n)(       )(\* ####[^#][^\n]*\n\n)(     )(\* [^#])/\1\2\3\2  \5/g' $mdoutput<br>sed -Ez -i 's/(\n)(     )(\* ###[^#][^\n]*\n\n)(     )(\* [^#])/\1\2\3\2  \5/g' $mdoutput<br>sed -Ez -i 's/(\n)( )(\* ###[^#][^\n]*\n\n)(     )(\* [^#])/\1\2\3\2    \5/g' $mdoutput<br>sed -Ez -i 's/(\n)(\* ###[^#][^\n]*\n\n)(     )(\* [^#])/\1\2\3 \4/g' $mdoutput<br>awk 'BEGIN{count=0; prevNR=0; prevChar=""} match($0,/^(( +)(\*)( +))([^#].*)/,a){if(prevNR!=0 &amp;&amp; NR == prevNR+2){print prevChar a[5]; prevNR = NR; } else{print; prevChar = a[1]; prevNR = NR} } !/^(( +)(\*)( +))([^#].*)/{ print } /^ +\* +#/{ prevChar = "" } ' $mdoutput &gt; tmp &amp;&amp; mv tmp $mdoutput<br>cat toc.md $mdoutput &gt; $mdfinal<br></td></tr></tbody></table>

 * ## \[image\]( Commands to convert google.doc to markdown)

     * ![](images/image142.png)

 * ## \[code\] View the .md file using grip

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>$ su (login as root)<br>$ pip install grip<br>$ grip -b README.md (view the file in firefox localhost:port)<br></td></tr></tbody></table>

 * ## \[code\] Important Note about Images && Split long images into smaller chunks (Because google docs reduce the image quality if images are big size)

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>When we download the files as  web page (zip, html) low resolution images are shown. <br><br>For that we want to keep the aspect ration of image to 903:753 (width:height). SO we plit the images into smaller images of aspect ratio 903:753<br><br>Two split an image into smaller images based on aspect ratio we have to do<br><br>convert -crop 903:753 input.png input_splited_%d.png<br><br>But the problem is we want some overlap so that if something is cut inbetween we still undestand<br><br>So what we do is first execute<br><br>convert -crop 903:753 input.png input_splited_%d.png <br><br>We will get number of cropped files. Assuming we got 4 cropped files<br><br>cropped_0.png<br>cropped_1.png<br>cropped_2.png<br>Cropped_3.png<br><br>We then execute<br><br>convert -crop 1x4+0+8@ input.png cropped_%d.png<br><br>1x4 will break the image into 4 vertical pieces and +0+8 will add an overlap of 8 pixels in top and bottom<br></td></tr></tbody></table>

     * \[code\] Everything put as a script

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>filename="cutom_user_code_model.png"; <br>rm -rf ~/croped<br>mkdir ~/croped<br>convert -crop 903:600 ${filename} ~/croped/crop_aspect_%d.png; <br>number_files=`ls -l ~/croped | grep -E "crop_aspect_*" | wc -l`<br>convert -crop 1x${number_files}+0+8@ ${filename} ~/croped/crop_grid_%d.png<br></td></tr></tbody></table>

 * ## PROCEDURE IN IMAGES

     * The Above procedure show in images

     * ### \[image\] Create a Sample\_doc file using google docs as follows:

       * ![](images/image110.png)

       * Can use Heading, Tables for code and can insert images

       * Note: Table should contain atleast two lines. If it contains only one line then it will not br show as table properly.

     * ### \[image\] After saving the google doc Download it as web\_page (html\_zipped)

       * ![](images/image215.png)

     * ### \[image\] Extract the files into a folder

       * ![](images/image47.png)

     * ### \[image\] Open a Terminal and go to this folder and run the below command

       * ![](images/image236.png)

       * The above command creates Sample\_doc\_toc.md. Note: $mdoutput and mdfinal should be different names

     * ### \[image\] To view the .md file we use the grip command

       * ![](images/image171.png)

     * ### \[image\] open [http://localhost:6419/](https://www.google.com/url?q=http://localhost:6419/&sa=D&ust=1571383143923000) in browser

       * ![](images/image219.png)

       * We have a good enough documentation.

 * ## How to take screenshot of code from sublime text:

     * In this documentation we have shown lot of screenshots from sublime text code. It was possible by a plugin called SublimeHighlight which converts the sublime text into html. Then open the html in chrome. And using Full Page Screen Capture ([https://chrome.google.com/webstore/detail/full-page-screen-capture/fdpohaocaechififmbbbbbknoalclacl?hl=en](https://www.google.com/url?q=https://chrome.google.com/webstore/detail/full-page-screen-capture/fdpohaocaechififmbbbbbknoalclacl?hl%3Den&sa=D&ust=1571383143924000)) we take the screenshot of the code and then split it using crop command discussed previously

     * After installing SublimeHighlight plugin in the sublime text, add the following to Default - Sublime Keymap

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>    {<br>        "keys": ["ctrl+alt+n"],<br>        "command": "export_html",<br>        "args": {<br>            "numbers": true,<br>            "wrap": 900,<br>            "view_open":true,<br>            "alternate_font_size": 12,<br>            "multi_select": true,<br>            "color_scheme": "/home/simha/.public_html/Monokai.tmTheme",<br>            "style_gutter": true,<br>        },<br>    }<br></td></tr></tbody></table>

     * \[image\] add the following to default-keybinding

     * ![](images/image235.png)

     * Now open any file in Sublime text and then press ctrl + alt + n

     * It will open another tab with the html code.

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>.code_page {<br>    background-color: #282923;<br>    font-family: "Monospace", "Courier", Monospace;<br>    font-size: 10pt;<br>    tab-size: 4;<br>}<br><br>In the html opened remove font-size, then in chrome the font looks big, so it will look like<br><br>.code_page {<br>    background-color: #282923;<br>    font-family: "Monospace", "Courier", Monospace;<br>    tab-size: 4;<br>}<br></td></tr></tbody></table>

     * To open in chrome use ctrl + alt + v (view in browser)

 * ## How to create a diff file for file between two commits

     * In some codes we want to show the diff so that we can know the lines added and lines deleted. For that we use the following command. Note use full file path

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>git diff -U10000 9f99377e8824afc902f37aa777b599b7e48d592e f6d3473fc2c5a3f4b653560da4ca54e1410ac6d7 /home/web_dev/django_basic_documentation/Pipfile &gt; ~/test.py<br><br>Note: we are saving the file as .py. Because .diff will not color the python code. It will only color red and green. Instead we want to show the code in python syntx highlighting with +++ and --- signs on the side.<br><br>9f99377e8824afc902f37aa777b599b7e48d592e and f6d3473fc2c5a3f4b653560da4ca54e1410ac6d7 are the commit between which we want to compare the file /home/web_dev/django_basic_documentation/Pipfile<br><br>We have to use -U10000 to show full files (even those which are not changed)<br><br>If we want to see only the difff without the non changed things then use<br><br>git diff 9f99377e8824afc902f37aa777b599b7e48d592e f6d3473fc2c5a3f4b653560da4ca54e1410ac6d7 /home/web_dev/django_basic_documentation/Pipfile &gt; ~/test.py<br><br>If we want to compare a file which is not in the git commit then we can do that by<br><br>git diff --no-index middleware_backup.py middleware.py &gt; /home/simha/test.py<br></td></tr></tbody></table>

     * Now this produces a file like below

     * ### \[image\] input (test.py) obtained from diff

       * ![](images/image5.png)

       * Using the below script we convert it as shown in the next image

     * ### \[code\] convertig to + to +++ and - to ---

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td> awk '{                                                                         <br>    gsub(/^/,"   ",$0)<br>    print $0<br>}' test.py &gt; test1.py<br><br>awk '{                                                                           <br>    gsub(/^   \+/,"++++",$0)<br>    print $0<br>}' test1.py &gt; test2.py<br><br>awk '{                                                                           <br>    gsub(/^   -/,"----",$0)<br>    print $0<br>}' test2.py &gt; test.py<br></td></tr></tbody></table>

     * ### \[image\] awk script

       * ![](images/image37.png)

     * ### \[image\] output (test.py after running the above script) we added +++ and ---

       * ![](images/image114.png)

* # FIRST COMMIT START:  

 * ## 1.We are using archlinux os and trying to setup a django project

 * ## 2.Installation pipenv:

     * ### 1.\[code\] Change or login to root

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>$ su (login to root)<br>Password:<br></td></tr></tbody></table>

     * ### 2.\[code\] Install pipenv

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>#gauranga<br>$ pip install pipenv<br></td></tr></tbody></table>

 * ## 3.Create a project directory and change into it

     * ### 1.\[code\] Create main project directory

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>#gauranga<br>$ mkdir /home/web_dev/django_basic_documentation<br></td></tr></tbody></table>

     * ### 2.\[code\] Change into project directory

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>#gauranga<br>$ cd /home/web_dev/django_basic_documentation<br></td></tr></tbody></table>

 * ## 4.Create a virtual env inside the project directory using pipenv

     * ### 1.Set PIPENV\_VENV\_IN\_PROJECT=1

       * (To make the virtual environment folder determininstic(.venv/) otherwise you will get a hash based directory(my\_project\_directory-some-hash-value)

       * Using PIPENV\_VENV\_IN\_PROJECT=true makes it more easier to activate virtual environment in a dockerfile which otherwise would depend on activating an environment based on some hash value pertaining the project.

       * pipenv shell is the UI for activation

       * #### \[code\]

         * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>#gauranga. And also ensure that .venv is in .gitignore file<br>$ export PIPENV_VENV_IN_PROJECT=1<br><br>Advantages of using virtualenv inside the project folder<br><ol><li>Sublime text will do the indexing. So it will be easy to navigate around the functions.</li><li>Docker file: </li></ol><br>Many Python packages only support installation in a virtual environment, in which case it's useful to be able to activate the venv inside a docker container<br><br>Pipenv intall creates a hash folder in home directory. In dockerfile when we want to use the python from virtual env its difficult to locate the hash folder which is auto generated. If we want to get the virtualenv path we have to try<br><br>ENV VIRTUALENV_PATH="$(pipenv --venv)" in my Dockerfile, but this seems messy.<br><br>So the solution is use PIPENV_VENV_IN_PROJECT=1, which will install the virtualenv in a .venv folder and then we can easily use the /path/.venv to access it<br><br>ENV PIPENV_VENV_IN_PROJECT 1<br>WORKDIR /var/lib/app<br>RUN pipenv install<br><br>Or<br><br>ENV PIPENV_VENV_IN_PROJECT true<br>ENV APP_PATH /code<br>ENV PATH $APP_PATH:$PATH<br>RUN pip install --upgrade pip<br>RUN pip install pipenv<br>WORKDIR $APP_PATH<br>RUN pipenv install<br><br>Or <br><br>WORKDIR /build<br>COPY Pipfile Pipfile.lock /build/<br>RUN bash -c 'PIPENV_VENV_IN_PROJECT=1 pipenv install'<br></td></tr></tbody></table>

     * ### 2.\[code\] create virtualenv and activate it

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>$ pipenv shell<br>Creating a virtualenv for this project…<br>Pipfile: /home/web_dev/django_basic_documentation/Pipfile<br>Using /usr/bin/python (3.7.3) to create virtualenv…<br>⠇ Creating virtual environment...Already using interpreter /usr/bin/python<br>Using base prefix '/usr'<br>New python executable in /home/simha/.local/share/virtualenvs/django_basic_documentation-4mWf8-Zv/bin/python<br>Installing setuptools, pip, wheel...<br>done.<br>✔ Successfully created virtual environment! <br>Virtualenv location: /home/simha/.local/share/virtualenvs/django_basic_documentation-4mWf8-Zv<br>Creating a Pipfile for this project…<br>Launching subshell in virtual environment…<br> . /home/simha/.local/share/virtualenvs/django_basic_documentation-4mWf8-Zv/bin/activate<br></td></tr></tbody></table>

     * ### 3.\[code\] Checking the files in the folder Pipfile is created

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>$ tree -R   <br>.<br>└── Pipfile<br>0 directories, 1 file<br></td></tr></tbody></table>

 * ## 5.In virtual env install Django

     * ### 1.\[code\] Install Django

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>#gauranga<br>$ pipenv install django<br></td></tr></tbody></table>

     * ### 2.\[code\] Checking the files in the folder Pipfile is created

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>$ tree <br>.<br>├── Pipfile<br>└── Pipfile.lock<br>0 directories, 2 files<br></td></tr></tbody></table>

     * ### 3.\[code\] Checking the packages installed by pipenv

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>$ pipenv graph<br><br>Django==2.2<br>  - pytz [required: Any, installed: 2018.9]<br>  - sqlparse [required: Any, installed: 0.3.0]<br></td></tr></tbody></table>

     * ### 4.\[code\] Activating python virtualenv. From the path of the directory pipenv know which virtualenv to activate. So go to the directory and run the below command

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>$ pipenv shell<br>Launching subshell in virtual environment…<br> . /home/simha/.local/share/virtualenvs/django_basic_documentation-4mWf8-Zv/bin/activate<br>$  . /home/simha/.local/share/virtualenvs/django_basic_documentation-4mWf8-Zv/bin/activate<br></td></tr></tbody></table>

 * ## 6.Check the version of Django

     * ### 1.\[code\] Check the django version

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>$ python -m django --version<br>2.2<br></td></tr></tbody></table>

 * ## 7.Check the version of django-admin

     * ### 1.\[code\] If you get the below error then exit the virtualenv and again activate the virtualenv

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>$ django-admin --version<br><br>Traceback (most recent call last):<br>  File "/usr/bin/django-admin", line 7, in &lt;module&gt;<br>    from django.core.management import execute_from_command_line<br>ModuleNotFoundError: No module named 'django'<br></td></tr></tbody></table>

     * ### 2.\[code\] If you get the above error: exit and reactivate the virtualenv

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>#gauranga<br>$ exit<br></td></tr></tbody></table>

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>#gauranga<br>$ pipenv shell<br></td></tr></tbody></table>

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>$ django-admin --version                                                                 <br>2.2<br></td></tr></tbody></table>

 * ## 8.Create a new DJango project

     * ### 1.\[code\] Use django-admin to create a project

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>#gauranga<br>$ django-admin startproject basic_django<br></td></tr></tbody></table>

     * ### After this the folder structure should look like this:

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>$ tree<br>.<br>├── basic_django<br>│   ├── basic_django<br>│   │   ├── __init__.py<br>│   │   ├── settings.py<br>│   │   ├── urls.py<br>│   │   └── wsgi.py<br>│   └── manage.py<br>├── Pipfile<br>└── Pipfile.lock<br><br>2 directories, 7 files<br></td></tr></tbody></table>

 * ## 9.Check the Django project is working

     *         

     * ### 1.\[code\] Change into the project directory which we have created

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>#gauranga<br>cd ./basic_django<br></td></tr></tbody></table>

       *  

     * ### 2.\[code\] Run the in temporary server

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>$ ./manage.py runserver (or $ ./manage.py runserver 127.0.0.1:8000)<br><br>Watching for file changes with StatReloader<br>Performing system checks...<br><br>System check identified no issues (0 silenced).<br><br>You have 17 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.<br>Run 'python manage.py migrate' to apply them.<br><br>April 04, 2019 - 18:35:28<br>Django version 2.2, using settings 'basic_django.settings'<br>Starting development server at http://127.0.0.1:8000/<br>Quit the server with CONTROL-C.<br>[04/Apr/2019 18:35:37] "GET / HTTP/1.1" 200 16348<br>[04/Apr/2019 18:35:37] "GET /static/admin/css/fonts.css HTTP/1.1" 200 423<br>[04/Apr/2019 18:35:38] "GET /static/admin/fonts/Roboto-Bold-webfont.woff HTTP/1.1" 200 86184<br>[04/Apr/2019 18:35:38] "GET /static/admin/fonts/Roboto-Regular-webfont.woff HTTP/1.1" 200 85876<br>[04/Apr/2019 18:35:38] "GET /static/admin/fonts/Roboto-Light-webfont.woff HTTP/1.1" 200 85692<br>Not Found: /favicon.ico<br>[04/Apr/2019 18:35:38] "GET /favicon.ico HTTP/1.1" 404 1978<br></td></tr></tbody></table>

     * ### 3.Open in firefox

       * Open [http://127.0.0.1:8080/](https://www.google.com/url?q=http://127.0.0.1:8080/&sa=D&ust=1571383143978000) in firefox or chrome and check. If we see below then the the installation is successful

       *         

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>The install worked successfully! Congratulations!<br>You are seeing this page because <a href="https://www.google.com/url?q=https://docs.djangoproject.com/en/2.2/ref/settings/%23debug&amp;sa=D&amp;ust=1571383143979000" class="c24">DEBUG=True</a> is in your settings file and you have not configured any URLs.<br><br></td></tr></tbody></table>

 * ## 10.Remove the secretkey from settings.py before we intialize first git commit after this section. Store the SecretKey for the time being somewhere

     * ###         \[code\] Edit: settings.py and change to the following and save

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>#gauranga<br>SECRET_KEY = 'dummysecretkey'<br></td></tr></tbody></table>

       *         

     * ### \[image\] (Showing settings.py with diff)

       * ![](images/image190.png)![](images/image153.png)![](images/image198.png)![](images/image210.png)![](images/image11.png)

 * ## 11.Create git repository and transfer to the github

     * ### 1.\[code\] Change into the main project directory

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>#gauranga<br>cd  /home/web_dev/django_basic_documentation<br></td></tr></tbody></table>

     * ### 2.\[code\] Create .gitignore with the following contents

       *         

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>#gauranga<br>touch  .gitignore <br></td></tr></tbody></table>

       *         NOTE:  Keep the gitignore final even later we want to add some more things here we can use git rebase -i --root and edit the first commit and change it and then update here also.

       *         \[code\] (.gitignore full code)

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td># Created by https://www.gitignore.io/api/pycharm,python,django<br># Edit at https://www.gitignore.io/?templates=pycharm,python,django<br><br>### Django ###<br>*.log<br>*.pot<br>*.pyc<br>__pycache__/<br>local_settings.py<br>db.sqlite3<br>media<br><br># If your build process includes running collectstatic, then you probably don't need or want to include staticfiles/<br># in your Git repository. Update and uncomment the following line accordingly.<br># &lt;django-project-name&gt;/staticfiles/<br>basic_django/staticfiles/<br><br>### Django.Python Stack ###<br># Byte-compiled / optimized / DLL files<br>*.py[cod]<br>*$py.class<br><br># C extensions<br>*.so<br><br># Distribution / packaging<br>.Python<br>build/<br>develop-eggs/<br>dist/<br>downloads/<br>eggs/<br>.eggs/<br>lib/<br>lib64/<br>parts/<br>sdist/<br>var/<br>wheels/<br>pip-wheel-metadata/<br>share/python-wheels/<br>*.egg-info/<br>.installed.cfg<br>*.egg<br>MANIFEST<br><br># PyInstaller<br>#  Usually these files are written by a python script from a template<br>#  before PyInstaller builds the exe, so as to inject date/other infos into it.<br>*.manifest<br>*.spec<br><br># Installer logs<br>pip-log.txt<br>pip-delete-this-directory.txt<br><br># Unit test / coverage reports<br>htmlcov/<br>.tox/<br>.nox/<br>.coverage<br>.coverage.*<br>.cache<br>nosetests.xml<br>coverage.xml<br>*.cover<br>.hypothesis/<br>.pytest_cache/<br><br># Translations<br>*.mo<br><br># Django stuff:<br><br># Flask stuff:<br>instance/<br>.webassets-cache<br><br># Scrapy stuff:<br>.scrapy<br><br># Sphinx documentation<br>docs/_build/<br><br># PyBuilder<br>target/<br><br># Jupyter Notebook<br>.ipynb_checkpoints<br><br># IPython<br>profile_default/<br>ipython_config.py<br><br># pyenv<br>.python-version<br><br># pipenv<br>#   According to pypa/pipenv#598, it is recommended to include Pipfile.lock in version control.<br>#   However, in case of collaboration, if having platform-specific dependencies or dependencies<br>#   having no cross-platform support, pipenv may install dependencies that don’t work, or not<br>#   install all needed dependencies.<br>#Pipfile.lock<br><br># celery beat schedule file<br>celerybeat-schedule<br><br># SageMath parsed files<br>*.sage.py<br><br># Environments<br>.env<br>.venv<br>env/<br>venv/<br>ENV/<br>env.bak/<br>venv.bak/<br><br># Spyder project settings<br>.spyderproject<br>.spyproject<br><br># Rope project settings<br>.ropeproject<br><br># mkdocs documentation<br>/site<br><br># mypy<br>.mypy_cache/<br>.dmypy.json<br>dmypy.json<br><br># Pyre type checker<br>.pyre/<br><br>### PyCharm ###<br># Covers JetBrains IDEs: IntelliJ, RubyMine, PhpStorm, AppCode, PyCharm, CLion, Android Studio and WebStorm<br># Reference: https://intellij-support.jetbrains.com/hc/en-us/articles/206544839<br><br># User-specific stuff<br>.idea/**/workspace.xml<br>.idea/**/tasks.xml<br>.idea/**/usage.statistics.xml<br>.idea/**/dictionaries<br>.idea/**/shelf<br><br># Generated files<br>.idea/**/contentModel.xml<br><br># Sensitive or high-churn files<br>.idea/**/dataSources/<br>.idea/**/dataSources.ids<br>.idea/**/dataSources.local.xml<br>.idea/**/sqlDataSources.xml<br>.idea/**/dynamic.xml<br>.idea/**/uiDesigner.xml<br>.idea/**/dbnavigator.xml<br><br># Gradle<br>.idea/**/gradle.xml<br>.idea/**/libraries<br><br># Gradle and Maven with auto-import<br># When using Gradle or Maven with auto-import, you should exclude module files,<br># since they will be recreated, and may cause churn.  Uncomment if using<br># auto-import.<br># .idea/modules.xml<br># .idea/*.iml<br># .idea/modules<br><br># CMake<br>cmake-build-*/<br><br># Mongo Explorer plugin<br>.idea/**/mongoSettings.xml<br><br># File-based project format<br>*.iws<br><br># IntelliJ<br>out/<br><br># mpeltonen/sbt-idea plugin<br>.idea_modules/<br><br># JIRA plugin<br>atlassian-ide-plugin.xml<br><br># Cursive Clojure plugin<br>.idea/replstate.xml<br><br># Crashlytics plugin (for Android Studio and IntelliJ)<br>com_crashlytics_export_strings.xml<br>crashlytics.properties<br>crashlytics-build.properties<br>fabric.properties<br><br># Editor-based Rest Client<br>.idea/httpRequests<br><br># Android studio 3.1+ serialized cache file<br>.idea/caches/build_file_checksums.ser<br><br># JetBrains templates<br>**___jb_tmp___<br><br>### PyCharm Patch ###<br># Comment Reason: https://github.com/joeblau/gitignore.io/issues/186#issuecomment-215987721<br><br># *.iml<br># modules.xml<br># .idea/misc.xml<br># *.ipr<br><br># Sonarlint plugin<br>.idea/sonarlint<br><br>### Python ###<br># Byte-compiled / optimized / DLL files<br><br># C extensions<br><br># Distribution / packaging<br><br># PyInstaller<br>#  Usually these files are written by a python script from a template<br>#  before PyInstaller builds the exe, so as to inject date/other infos into it.<br><br># Installer logs<br><br># Unit test / coverage reports<br><br># Translations<br><br># Django stuff:<br><br># Flask stuff:<br><br># Scrapy stuff:<br><br># Sphinx documentation<br><br># PyBuilder<br><br># Jupyter Notebook<br><br># IPython<br>*/.ipynb_checkpoints/*.ipynb<br>*.ipynb<br><br># pyenv<br><br># pipenv<br>#   According to pypa/pipenv#598, it is recommended to include Pipfile.lock in version control.<br>#   However, in case of collaboration, if having platform-specific dependencies or dependencies<br>#   having no cross-platform support, pipenv may install dependencies that don’t work, or not<br>#   install all needed dependencies.<br><br># celery beat schedule file<br><br># SageMath parsed files<br><br># Environments<br><br># Spyder project settings<br><br># Rope project settings<br><br># mkdocs documentation<br><br># mypy<br><br># Pyre type checker<br><br># End of https://www.gitignore.io/api/pycharm,python,django<br><br></td></tr></tbody></table>

     * ### \[image\] (.gitignore full code)

       * ![](images/image228.png)![](images/image54.png)![](images/image118.png)![](images/image109.png)![](images/image193.png)![](images/image59.png)![](images/image175.png)

     * ### Project tree (showing .gitignore)

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>$ tree -a (-a to show hidden files)<br>.<br>├── basic_django<br>│   ├── basic_django<br>│   │   ├── __init__.py<br>│   │   ├── settings.py<br>│   │   ├── urls.py<br>│   │   └── wsgi.py<br>│   ├── db.sqlite3<br>│   └── manage.py<br>├── .gitignore<br>├── Pipfile<br>└── Pipfile.lock<br><br>2 directories, 9 files<br></td></tr></tbody></table>

     * ### 3.\[theory\] Git config:

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>Git comes with a tool called git config that lets you get and set configuration variables that control all aspects of how Git looks and operates. These variables can be stored in three different places:<br><ol><li>/etc/gitconfig file: Contains values applied to every user on the system and all their repositories. If you pass the option --system to git config, it reads and writes from this file specifically. (Because this is a system configuration file, you would need administrative or superuser privilege to make changes to it.)</li><li>~/.gitconfig or ~/.config/git/config file: Values specific personally to you, the user. You can make Git read and write to this file specifically by passing the --global option, and this affects all of the repositories you work with on your system.</li><li>config file in the Git directory (that is, .git/config) of whatever repository you’re currently using: Specific to that single repository. You can force Git to read from and write to this file with the --local option, but that is in fact the default. (Unsurprisingly, you need to be located somewhere in a Git repository for this option to work properly.)</li></ol>Each level overrides values in the previous level, so values in .git/config trump those in /etc/gitconfig.<br></td></tr></tbody></table>

       * You can view all of your settings and where they are coming from using:

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>$ git config --list --show-origin<br><br>file:/home/simha/.gitconfig     user.name= xxx<br>file:/home/simha/.gitconfig     user.email= xxx<br>file:/home/simha/.gitconfig    xxx= xxx<br>file:/home/simha/.gitconfig     core.autocrlf=input<br>file:.git/config        core.repositoryformatversion=0<br>file:.git/config        core.filemode=true<br>file:.git/config        core.bare=false<br>file:.git/config        core.logallrefupdates=true<br></td></tr></tbody></table>

     * ### 4.\[code\] Intialize git repository

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>#  git init .<br>Initialized empty Git repository in /home/web_dev/django_basic_documentation/.git/<br></td></tr></tbody></table>

     * ### 12.Git steps to commit and push to github

     * ### \[code\] Staging the files: (git add . or git add -A)

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>#gauranga<br>$ git add .  (use this if we want to only add changes in this folder and folders below recursively)<br></td></tr></tbody></table>

       * OR 

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>#gauranga<br>$ git add -A  (use this inside any folder it will add all the filed even from previous folders)<br></td></tr></tbody></table>

     * ### \[code\] Check the status

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>#  git status<br>On branch master<br><br>No commits yet<br><br>Changes to be committed:<br>  (use "git rm --cached &lt;file&gt;..." to unstage)<br><br>        new file:   .gitignore<br>        new file:   Pipfile<br>        new file:   Pipfile.lock<br>        new file:   basic_django/basic_django/__init__.py<br>        new file:   basic_django/basic_django/settings.py<br>        new file:   basic_django/basic_django/urls.py<br>        new file:   basic_django/basic_django/wsgi.py<br>        new file:   basic_django/manage.py<br><br><br></td></tr></tbody></table>

     * ### 13.\[code\] Git commit  (dont use git commit -am “message” it will not add new files)

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>$ git commit -m "First Commit: Fresh virtualenv with pipenv and install django and remove SECRETKEY"<br>                         <br>[master (root-commit) 7931de3] First Commit: Fresh virtualenv with pipenv and install django and remove SECRETKEY<br> 8 files changed, 508 insertions(+)<br> create mode 100644 .gitignore<br> create mode 100644 Pipfile<br> create mode 100644 Pipfile.lock<br> create mode 100644 basic_django/basic_django/__init__.py<br> create mode 100644 basic_django/basic_django/settings.py<br> create mode 100644 basic_django/basic_django/urls.py<br> create mode 100644 basic_django/basic_django/wsgi.py<br> create mode 100755 basic_django/manage.py<br></td></tr></tbody></table>

       * Refer to gitdoc in ./gitdoc folder of how to do changes after commit etc

 * ## 14.Transfer to the github use sshkeys

     * ### 1.\[code\] Generate an ssh-key and passphrase in the system using

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>$ ssh-keygen <br><br>        Generating public/private rsa key pair.<br>        Enter file in which to save the key (/home/simha/.ssh/id_rsa): <br>        Enter passphrase (empty for no passphrase):<br>        Enter same passphrase again: <br>        Your identification has been saved in /home/simha/.ssh/id_rsa.<br>        Your public key has been saved in /home/simha/.ssh/id_rsa.pub.<br>        The key fingerprint is:<br>        SHA256:RHlQB1RaKn+wcyhVlICVIVeCx+M7ifVbCO1pHifT0Nk simha@gauranga<br>        The key's randomart image is:<br>        +---[RSA 2048]----+<br>        |        +XXOB.   |<br>        |       .+o*B.    |<br>        |        o+=o . o |<br>        |       . +++o o E|<br>        |        So=*o=   |<br>        |        ..++X +  |<br>        |           + B   |<br>        |            o    |<br>        |                 |<br>        +----[SHA256]-----+<br><br><br></td></tr></tbody></table>

     * ### 2.\[code\] view the ssh key

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>cat ~/.ssh/id_rsa.pub<br>  Ssh-rsa ………….. Kjkajksdhkj j h<br></td></tr></tbody></table>

     * ### 3.\[code\] Copy the ssh key into github

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>#gauranga<br>Copy the ssh key above and go to github.com → Settings -&gt; ssh and gpg keys -&gt; New ssh key -&gt; paste the ssh key from the above command and put some title (lenovolaptop) and then save<br></td></tr></tbody></table>

     * ### 4.\[code\] Check the ssh connection

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>$ ssh -T git@github.com<br><br>        Warning: Permanently added the RSA host key for IP address '192.30.253.113' to the list of known hosts.<br>        Enter passphrase for key '/home/simha/.ssh/id_rsa': <br>        Hi sant527! You've successfully authenticated, but GitHub does not provide shell access.<br><br><br></td></tr></tbody></table>

     * ### 5.\[code\] Get the ssh url from github.

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>In the repo of github -&gt; clone and download -&gt; Clone with SSH <br><h4 id="h.359mi62o0kfx" class="c6 c60"></h4>Clone with SSH <br>Use an SSH key and passphrase from account.<br>git@github.com:sant527/django_basic_documentation.git<br></td></tr></tbody></table>

     * ### 6.\[code\] Add the ssh url to remote in git

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>#gauranga<br>$ git remote add basicdjango git@github.com:sant527/django_basic_documentation.git<br></td></tr></tbody></table>

       * This command simply means "you are adding the location of your repository on a remote machine/server where you wish to push your files?". 

     * ### 7.\[code\] Verify remote urls

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>$ git remote -v<br>basicdjango        git@github.com:sant527/django_basic_documentation.git (fetch)<br>basicdjango        git@github.com:sant527/django_basic_documentation.git (push)<br></td></tr></tbody></table>

     * ### 8.\[code\]  Reset the remote url , if one has added multiple remote urls (not required if there is only one remote url in git remote -v

       *         

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>#gauranga<br>$ git remote set-url basicdjango git@github.com:sant527/django_basic_documentation.git<br></td></tr></tbody></table>

       * The above is required if git push is sending to some other remote-url, then we want to tell git by set-url to which url it should push

 * ## 15.Git push

     * ### 9.\[code\] First time git push with setting up the --set-upstream (-u) and which branch

       *         After Adding the remote url, then we try to git push, it gives error

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>$ git push<br>        fatal: No configured push destination.<br>        Either specify the URL from the command-line or configure a remote repository using<br>            git remote add &lt;name&gt; &lt;url&gt;<br>        and then push using the remote name<br>            git push &lt;name&gt;<br></td></tr></tbody></table>

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>$ git push basicdjango<br>fatal: The current branch master has no upstream branch.<br>To push the current branch and set the remote as upstream, use<br>    git push --set-upstream basicdjango master<br><br></td></tr></tbody></table>

       *         In case of upstream we have to set git push by telling which upstream the local branch should be pushed to 

       *         Understanding the error: 

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>git push --set-upstream basicdjango master<br><br>git push (remote location /other local branch) (localbranch)<br><br>Here master (is the local branch and also the current branch name)<br><br>Remotebranch = --set-upstream remotename (from git remote add remotename “url”)<br></td></tr></tbody></table>

       *         So first time runt the below

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>$ git push -u basicdjango master<br><br>Ssh key<br>Passphrase:                                                       <br>Enumerating objects: 12, done.<br>Counting objects: 100% (12/12), done.<br>Delta compression using up to 4 threads<br>Compressing objects: 100% (11/11), done.<br>Writing objects: 100% (12/12), 5.28 KiB | 5.28 MiB/s, done.<br>Total 12 (delta 0), reused 0 (delta 0)<br>To https://github.com/sant527/django_basic_documentation.git<br> * [new branch]      master -&gt; master<br>Branch 'master' set up to track remote branch 'master' from 'basicdjango'.<br></td></tr></tbody></table>

       * From Next time onwards

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>#gauranga<br>git push<br></td></tr></tbody></table>

 * ## \[Git clone: Sometimes we may have to clone back from the github to undo some changes then do

     * ### \[code\]

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>$ git clone git@github.com:sant527/django_basic_documentation.git .                            <br>Directory must be empty<br></td></tr></tbody></table>

 * ## 16.GIT LOG

     *         [git log](https://www.google.com/url?q=http://git-scm.com/docs/git-log&sa=D&ust=1571383144081000) shows the commit log accessible from the refs (heads, tags, remotes)

     * ### \[code\] Commands to view git log and git reflog

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>--git log ---<br>git --no-pager log --graph --abbrev-commit --decorate --format=format:'%C(bold blue)%h%C(reset) - %C(bold cyan)%aD%C(reset) %C(bold green)(%ar)%C(reset)%C(auto)%d%C(reset)%n''          %C(green)%s%C(reset) %C(dim magenta)- %an%C(reset)' --all<br><br>For Gui based use:<br>Gitk --all (it will show gui)<br></td></tr></tbody></table>

     * ### \[code\] How do I prevent git diff from using a pager?

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>Use --no-pager <br>git --no-pager  log<br></td></tr></tbody></table>

* # FIRST COMMIT END

* # SECOND COMMIT START

 * ## 1.Create Postgresql User and Database

     * ### 1.\[code\] Change to root

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>$ su<br>Password: <br></td></tr></tbody></table>

     * ### 2.\[code\] Change to postgres user

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>#  su - postgres                                                                                                                                     <br>[postgres@gauranga ~]$ <br></td></tr></tbody></table>

     * ### 3.\[code\] Create database user 

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>#gauranga<br># psql -v ON_ERROR_STOP=1 -d postgres -c "CREATE USER someusername WITH PASSWORD 'somepasswd';" <br></td></tr></tbody></table>

     * ### \[code\] Create database with user as owner

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>#gauranga<br>psql -v ON_ERROR_STOP=1 -d postgres -c "CREATE DATABASE basicdjangodb OWNER someusername;"<br></td></tr></tbody></table>

 * ## 2.\[code\] Install the PostgreSQL Django adapter, psycopg2

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>$ pipenv install psycopg2<br><br>Installing psycopg2…<br>Adding psycopg2 to Pipfile's [packages]…<br>✔ Installation Succeeded <br>Pipfile.lock (70c6eb) out of date, updating to (4f9dd2)…<br>Locking [dev-packages] dependencies…<br>Locking [packages] dependencies…<br>✔ Success! <br>Updated Pipfile.lock (70c6eb)!<br>Installing dependencies from Pipfile.lock (70c6eb)…<br>  🐍   ▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉ 4/4 — 00:00:01<br></td></tr></tbody></table>

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>$ pipenv graph<br><br>Django==2.2<br>  - pytz [required: Any, installed: 2018.9]<br>  - sqlparse [required: Any, installed: 0.3.0]<br>psycopg2==2.8<br></td></tr></tbody></table>

 * ## 3.\[theory\] Django settings.py for development and production and protect sensitive data

     * Django has a pretty good system in place for handling configuration:  the settings file. It’s the one place you go to set configuration variables  for your app. There are a couple of common scenarios however that the settings file doesn’t handle super well.  

     * Namely sensitive settings and different environments (dev, prod, staging).

     * 1) Sensitive Settings

     * 2) different environments (dev, prod, staging)

     * 1) Sensitive Settings

     *   -- secret key

     *   -- database password

     *   -- don’t want sensitive settings hardcoded

     * 2) different environmens

     *   -- different databases (in local and prod)

     *   -- different Debug setting

     * Approches used in the past:

     * 1) setting environmental variables

     * 2) multiple settings

     * Solution:

     * -- django-environ

     *  -- allowing us to load configuration variables from a file

 * ## 4.\[code\] Install the django-environ in the virtual env

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>#gauranga<br>$ pipenv install django-environ <br></td></tr></tbody></table>

     * NOTE: No need to add it to INSTALLED\_APPS.

 * ## 4.Generate random SECRETKEY

     * ### \[code\] Method 1: cd into the app directory

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>Open a Django shell with python manage.py shell and do the following to create a secure random secret key in Django 2.1:<br>python manage.py shell<br>&gt;&gt;&gt; from django.core.management.utils import get_random_secret_key <br>&gt;&gt;&gt; get_random_secret_key() '[GENERATED KEY]' <br>&gt;&gt;&gt;<br>Note: The &gt;&gt;&gt; represents the shell prompt, and should not be typed.<br></td></tr></tbody></table>

     * ### \[code\] Method 2: from python

       * |                                                                                                                                                                                      |

       * | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |

       * | $ python -c 'import random; result = "".join(\[random.choice("abcdefghijklmnopqrstuvwxyz0123456789\!@\#$%^&\*(-\_=+)") for i in range(50)\]); print(result)' |

 * ## 5.Setup variables Using .env file in (note .env should be added to .gitignore)

     * ### 1.\[code\] Create a .env file

       *         

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>cd /home/web_dev/basic_django_documentation/basic_django<br>vi .env (and paste in it the below content)<br></td></tr></tbody></table>

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td># even we keep the variable empty but if its used in the settigns.py (e.g env('ALLOWED_HOSTS')) it has to be mentioned here else it will show error. Thats why we use environ.Env( ALLOWED_HOSTS=(list, ['127.0.0.1:8000'])) to set default value in the settings.py<br># never use comments on the same line eg:<br># EMAIL_HOST_PASSWORD = 'somepass' #enter pass<br># in settings env('EMAIL_HOST_PASSWORD') value is ('somepass' #enter pass). Even (#enter pass) is included. So it does not recognize # as comment. So put comments only on the top or bottom of line<br><br>DEBUG=on<br><br>SECRET_KEY='somekey'<br><br>DATABASE_URL=psql://user:pass@127.0.0.1:5432/dbname<br><br>ALLOWED_HOSTS=<br><br># using gmail to send emails via smtp<br>EMAIL_HOST_USER='username@gmail.com'<br># this is app password not the regular gmail password. Before this enable 2 step verfication<br>EMAIL_HOST_PASSWORD='password'<br><br># used as recipient email in send_email for testing in test_8commit() in django_basic_documentation/basic_django/basic_django/views.py<br>TESTING_EMAIL='reciever@gmail.com'<br></td></tr></tbody></table>

       *         The EMAIL\_HOST\_USER, EMAIL\_HOST\_PASSWORD and  TESTING\_EMAIL will be discussed in future commits. But here we can leave them empty.

     * ### 2.\[code\] Save the .env file in a personal folder outside the project dir. Incase you deleted proj directory you can get back the .env file

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>cd /home/web_dev<br>mkdir env_basic_django_documentation<br>cp /home/web_dev/basic_django_documentation/basic_django/.env /home/web_dev/env_basic_django_documentation<br></td></tr></tbody></table>

       *                       The below shows how the postgres configuration just for an idea

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>DATABASES = {<br>    'default': {<br>        'ENGINE': 'django.db.backends.postgresql',<br>        'NAME': 'db_name',                      <br>        'USER': 'db_user',<br>        'PASSWORD': 'db_user_password',<br>        'HOST': '',<br>        'PORT': 'db_port_number',<br>    }<br>}<br><br></td></tr></tbody></table>

     * ### 3.\[code\] Access those env variables inside settings.py

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>#################<br><br>#using .env to store important info and keep single settings.py file and change<br>#the .env variables as per development and production requirements<br><br>#if we use  (e.g env('ALLOWED_HOSTS')) in the settigns.py it has to be mentioned<br>#in .env file even we keep the variable empty in the .env else it will show<br>#error. Thats why we use environ.Env( ALLOWED_HOSTS=(list, ['127.0.0.1:8000']))<br>#to set default value in the settings.py in case its left empty.<br><br>#For accessing env variables from .env inside settings.py <br>#step 1<br>import environ<br><br>#step 2<br># define env as below. Here mention all the defaults we want to have if we leave<br># variables empty in .env file. But this will not check if the variable is<br># defined in .env file or not<br>env = environ.Env(<br>    # set casting, default value<br>    DEBUG=(bool, False),<br>    ALLOWED_HOSTS=(list, ['127.0.0.1:8000']),<br>)<br><br># step 3<br># reading .env file<br>environ.Env.read_env()<br><br>#step 4<br>#getting the env variable value from the KEY. This will check the .env<br>#file for the variable. If its not defined then it will show error. If its empty<br>#and its default is defined then it pics the default value else shows empty. <br>#Eg: SECRET_KEY = env('SECRET_KEY')<br><br>##################<br><br><br># Now replace the following in the settings.py file manually<br><br>SECRET_KEY = env('SECRET_KEY')<br><br>DEBUG = env('DEBUG')<br><br>ALLOWED_HOSTS = env('ALLOWED_HOSTS')<br><br>DATABASES = {<br>    # read os.environ['DATABASE_URL'] and raises ImproperlyConfigured exception if not found<br>    'default': env.db(),  <br>    # env.db() is a short form of env.db(‘DATABASE_URL', default='psql:////tmp/my-tmp-sqlite.db')<br>}<br></td></tr></tbody></table>

     * ### \[code\] FULL settings.py file

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>"""<br>Django settings for basic_django project.<br><br>Generated by 'django-admin startproject' using Django 2.2.6.<br><br>For more information on this file, see<br>https://docs.djangoproject.com/en/2.2/topics/settings/<br><br>For the full list of settings and their values, see<br>https://docs.djangoproject.com/en/2.2/ref/settings/<br>"""<br><br>import os<br><br># Build paths inside the project like this: os.path.join(BASE_DIR, ...)<br>BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))<br><br><br># Quick-start development settings - unsuitable for production<br># See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/<br><br>#################<br><br>#using .env to store important info and keep single settings.py file and change<br>#the .env variables as per development and production requirements<br><br>#if we use  (e.g env('ALLOWED_HOSTS')) in the settigns.py it has to be mentioned<br>#in .env file even we keep the variable empty in the .env else it will show<br>#error. Thats why we use environ.Env( ALLOWED_HOSTS=(list, ['127.0.0.1:8000']))<br>#to set default value in the settings.py in case its left empty.<br><br>#For accessing env variables from .env inside settings.py <br>#step 1<br>import environ<br><br>#step 2<br># define env as below. Here mention all the defaults we want to have if we leave<br># variables empty in .env file. But this will not check if the variable is<br># defined in .env file or not<br>env = environ.Env(<br>    # set casting, default value<br>    DEBUG=(bool, False),<br>    ALLOWED_HOSTS=(list, ['127.0.0.1:8000']),<br>)<br><br># step 3<br># reading .env file<br>environ.Env.read_env()<br><br>#step 4<br>#getting the env variable value from the KEY. This will check the .env<br>#file for the variable. If its not defined then it will show error. If its empty<br>#and its default is defined then it pics the default value else shows empty. <br>#Eg: SECRET_KEY = env('SECRET_KEY')<br><br>##################<br><br><br># SECURITY WARNING: keep the secret key used in production secret!<br>SECRET_KEY = env('SECRET_KEY')<br><br># SECURITY WARNING: don't run with debug turned on in production!<br>DEBUG = env('DEBUG')<br><br>ALLOWED_HOSTS = env('ALLOWED_HOSTS')<br><br><br># Application definition<br><br>INSTALLED_APPS = [<br>    'django.contrib.admin',<br>    'django.contrib.auth',<br>    'django.contrib.contenttypes',<br>    'django.contrib.sessions',<br>    'django.contrib.messages',<br>    'django.contrib.staticfiles',<br>]<br><br>MIDDLEWARE = [<br>    'django.middleware.security.SecurityMiddleware',<br>    'django.contrib.sessions.middleware.SessionMiddleware',<br>    'django.middleware.common.CommonMiddleware',<br>    'django.middleware.csrf.CsrfViewMiddleware',<br>    'django.contrib.auth.middleware.AuthenticationMiddleware',<br>    'django.contrib.messages.middleware.MessageMiddleware',<br>    'django.middleware.clickjacking.XFrameOptionsMiddleware',<br>]<br><br>ROOT_URLCONF = 'basic_django.urls'<br><br>TEMPLATES = [<br>    {<br>        'BACKEND': 'django.template.backends.django.DjangoTemplates',<br>        'DIRS': [],<br>        'APP_DIRS': True,<br>        'OPTIONS': {<br>            'context_processors': [<br>                'django.template.context_processors.debug',<br>                'django.template.context_processors.request',<br>                'django.contrib.auth.context_processors.auth',<br>                'django.contrib.messages.context_processors.messages',<br>            ],<br>        },<br>    },<br>]<br><br>WSGI_APPLICATION = 'basic_django.wsgi.application'<br><br><br># Database<br># https://docs.djangoproject.com/en/2.2/ref/settings/#databases<br><br>### DATABASES = {<br>###     'default': {<br>###         'ENGINE': 'django.db.backends.sqlite3',<br>###         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),<br>###     }<br>### }<br><br>DATABASES = {<br>    # read os.environ['DATABASE_URL'] and raises ImproperlyConfigured exception if not found<br>    'default': env.db(),  <br>    # env.db() is a short form of env.db(‘DATABASE_URL', default='psql:////tmp/my-tmp-sqlite.db')<br>}<br><br><br><br># Password validation<br># https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators<br><br>AUTH_PASSWORD_VALIDATORS = [<br>    {<br>        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',<br>    },<br>    {<br>        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',<br>    },<br>    {<br>        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',<br>    },<br>    {<br>        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',<br>    },<br>]<br><br><br># Internationalization<br># https://docs.djangoproject.com/en/2.2/topics/i18n/<br><br>LANGUAGE_CODE = 'en-us'<br><br>TIME_ZONE = 'UTC'<br><br>USE_I18N = True<br><br>USE_L10N = True<br><br>USE_TZ = True<br><br><br># Static files (CSS, JavaScript, Images)<br># https://docs.djangoproject.com/en/2.2/howto/static-files/<br><br>STATIC_URL = '/static/'<br></td></tr></tbody></table>

     * ### Images of settings.py with .env variables

       * #### \[image\] navigation

         * ![](images/image41.png)

       * #### \[image\] Settings.py full

         * ![](images/image208.png)![](images/image232.png)![](images/image117.png)![](images/image143.png)

       * #### \[image\] settings.pyf with diff

         * ![](images/image80.png)![](images/image119.png)![](images/image24.png)![](images/image146.png)![](images/image121.png)![](images/image197.png)

 * ## 6.\[code\] Create a .env.example file so that other will know add theirs.

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>#gauranga<br>cd /home/web_dev/django_basic_documentation/basic_django/basic_django<br></td></tr></tbody></table>

     *         

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>#gauranga<br>touch .env.example<br></td></tr></tbody></table>

     *         Add the below contents to .env.example

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td># even we keep the variable empty but if its used in the settigns.py (e.g env('ALLOWED_HOSTS')) it has to be mentioned here else it will show error. Thats why we use environ.Env( ALLOWED_HOSTS=(list, ['127.0.0.1:8000'])) to set default value in the settings.py<br># never use comments on the same line eg:<br># EMAIL_HOST_PASSWORD = 'somepass' #enter pass<br># in settings env('EMAIL_HOST_PASSWORD') value is ('somepass' #enter pass). Even (#enter pass) is included. So it does not recognize # as comment. So put comments only on the top or bottom of line<br><br>DEBUG=on<br><br>SECRET_KEY='somekey'<br><br>DATABASE_URL=psql://user:pass@127.0.0.1:5432/dbname<br><br>ALLOWED_HOSTS=<br><br># using gmail to send emails via smtp<br>EMAIL_HOST_USER='username@gmail.com'<br># this is app password not the regular gmail password. Before this enable 2 step verfication<br>EMAIL_HOST_PASSWORD='password'<br><br># used as recipient email in send_email for testing in test_8commit() in django_basic_documentation/basic_django/basic_django/views.py<br>TESTING_EMAIL='reciever@gmail.com'<br></td></tr></tbody></table>

     * ### \[image\] .env.example file

       * ![](images/image20.png)

 * ##         Project tree

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>$ tree -a -I '.git'  (we dont want to show the git directories)<br>.<br>├── basic_django<br>│   ├── basic_django<br>│   │   ├── .env<br>│   │   ├── .env.example<br>│   │   ├── __init__.py<br>│   │   ├── settings.py<br>│   │   ├── urls.py<br>│   │   └── wsgi.py<br>│   ├── db.sqlite3<br>│   └── manage.py<br>├── .gitignore<br>├── Pipfile<br>└── Pipfile.lock<br><br>2 directories, 11 files<br></td></tr></tbody></table>

* # SECOND COMMIT END

* # THIRD COMMIT START

 * ## AIM OF THIRD - Some important tools: install django-extensions,ipython, jupyter, pretty printing dicts or objects by using dir(), runserver\_plus and werkzeug, graph models, django\_querycount, pudb (debugger), logging, traceback

 * ## Pretty printing Objects and SQL with color using json.dumps, sqlparser and pygments, connections, cursor:

     * Aim:

     * 1.  Pretty print a dictionary

     * 2.  Pretty print obj using dir(obj)

     * 3.  Pretty print sql string

     * 4.  Pretty print sql from query set (if using postgresql)

     * 5.  Pretty print sql from query set (is not using postgresql)

     *         Note: One more way to see sql is by using logging “django.db.backends”. Its mentioned later

     *             Note: if DEBUG = True, then all of your queries are logged else not. So logging “django.db.backends”. Shows sql only when DEBUG = True, its inbuilt.

     * ### \[code\] Install sqlparse and pygments

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>$ pipenv install sqlparse  # not using --dev. we install it in production also since we import it in code<br>$ pipenv install pygments # not using --dev. we install it in production also since we import it in code<br></td></tr></tbody></table>

     * ### \[code\] Custom functions for pretty pringing

       * Add the following functions in the settings.py.

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>#######################################################<br># Pretty printing object and sql by various means<br>#######################################################<br>#we found that if key is byte string then json.dumps will throw error So we have to convert the dict<br># recursive key as string conversion for byte keys<br>#https://stackoverflow.com/a/57014404/2897115<br><br>## '_preconf_set_by_auto': {'result_backend', 'broker_url'}<br>## the above will raise error: AttributeError: 'str' object has no attribute 'items'<br>## list = [1,3,4] To declare a tuple, we use brackets.<br>## tuples = (1, 2, "a") To declare a tuple, we use parentheses.<br>## sets = {1,2,3} declare a set. Use curly braces<br>def keys_string(d):<br>    rval = {}<br>    if not isinstance(d, dict):<br>        if isinstance(d,(tuple,list,set)):<br>            v = [keys_string(x) for x in d]<br>            return v<br>        else:<br>            return d<br>    for k,v in d.items():<br>        if isinstance(k,bytes):<br>            k = k.decode()<br>        if isinstance(v,dict):<br>            v = keys_string(v)<br>        elif isinstance(v,(tuple,list,set)):<br>            v = [keys_string(x) for x in v]<br>        rval[k] = v<br>    return rval<br><br>def json_dumps_default(obj):<br>    repr_obj = repr(obj)<br>    str_obj = str(obj)<br><br>    if repr_obj == str_obj:<br>        return repr_obj<br>    else:<br>        return repr_obj,f"STR: {str_obj}"<br><br># get_object: pretty print using dir(obj) and then its properties<br>def pp_odir_getobject(obj):<br>    if isinstance(obj,dict):<br>        return keys_string(obj)<br>    if isinstance(obj,(tuple,list,set)):<br>        return keys_string(obj)<br><br>    #c_dict = {k: getattr(obj, k) for k in dir(obj)} # this gives all the properties listed using dir(c)<br><br>    # we are not using the above is because if there are except it stops<br>    c_dict = {<br>                '00_METHODS********************************************************************************':{},<br>                "01_UNDESCORE******************************************************************************":{},<br>                "02_OTHERS*********************************************************************************":{},<br>                "03_EXCEPTIONS*****************************************************************************":{},<br>                }<br>    for key in dir(obj):<br>        try:<br>            attr_obj = getattr(obj, key)<br>            if callable(attr_obj):<br>            #if inspect.ismethod(attr_obj):<br>                c_dict['00_METHODS********************************************************************************'][key] = attr_obj<br>            else:<br>                if key.startswith("_"):<br>                    c_dict['01_UNDESCORE******************************************************************************'][key] = attr_obj<br>                else:<br>                    c_dict['02_OTHERS*********************************************************************************'][key] = attr_obj<br>        except Exception as x:<br>            c_dict['03_EXCEPTIONS*****************************************************************************'][key] = x<br>    return keys_string(c_dict)<br><br><br># pretty print using dir(obj) and then its properties<br>def pp_odir(obj):<br><br>    ##  json.dumps(queryset) in Jupyter runs lot of sqls if the object is query set so we want to avoid that. It work fine with views.py<br>    ## .So we want to stop logging before json_str and continue back with its state after<br>    import logging<br>    logger_database = logging.getLogger("django.db.backends")<br>    try:<br>        log_filt_state=logger_database.filters[0].state<br>        logger_database.filters[0].close()<br>    except:<br>        pass<br><br>    c_dict_flattened = pp_odir_getobject(obj)<br><br>    import json<br>    from pygments import highlight<br>    from pygments.lexers import JsonLexer<br>    from pygments.formatters import TerminalTrueColorFormatter<br>    #Before passing the dict we want to avoid any byte string keys so keys_string(c_dict)<br>    json_str=json.dumps(c_dict_flattened, indent=4, sort_keys=True, default=json_dumps_default)<br><br>    try:<br>        # based on the logging status continue after    <br>        if log_filt_state == 'open':<br>            logger_database.filters[0].open()<br>    except:<br>        pass<br><br>    return highlight(json_str, JsonLexer(), TerminalTrueColorFormatter())<br><br><br># pretty print dictionary<br>def pp_dict(dict):<br>    import json<br>    from pygments import highlight<br>    from pygments.lexers import JsonLexer<br>    from pygments.formatters import TerminalTrueColorFormatter<br>    # json.dumps (needs a dict item and pass default=str to avoid typeError)<br>    json_str=json.dumps(keys_string(dict), indent=4, sort_keys=True, default=json_dumps_default)<br>    return highlight(json_str, JsonLexer(), TerminalTrueColorFormatter())<br><br><br>def pp_sql_sql(sql):<br>    import sqlparse<br>    import pygments<br>    from pygments.lexers import SqlLexer<br>    from pygments.formatters import TerminalTrueColorFormatter<br>    # format using sqlparser<br>    sql = sqlparse.format(sql, reindent=True)<br>    # color it using pygments<br>    sql = pygments.highlight(sql,SqlLexer(),TerminalTrueColorFormatter())<br>    return sql<br><br># pretty print sql query from queryset using mogrify(available only for Psycopg)<br># Advantage: It does not execute any sql to get the sql<br>def pp_sql_query_pg(qs):<br>    from django.db import connections<br>    # Get a cursor tied to the database of queryset<br>    cursor = connections[qs.db].cursor()<br><br>    # Get the query SQL and parameters to be passed into psycopg2<br>    query, params = qs.query.sql_with_params()<br><br>    # use mogrify: Return a query string after arguments binding. The string returned is exactly the one that would be sent to the database running the execute() method or similar.<br>    # mogrify is not a method defined by the Python DB API, but instead an add-on of the Psycopg driver. It does not exist for MySql<br>    sql = cursor.mogrify(query, params)<br><br>    # Then format it using sqlparser and color it using pygment<br>    import sqlparse<br>    import pygments<br>    from pygments.lexers import SqlLexer<br>    from pygments.formatters import TerminalTrueColorFormatter<br>    # format using sqlparser<br>    sql = sqlparse.format(sql, reindent=True)<br>    # color it using pygments<br>    sql = pygments.highlight(sql,SqlLexer(),TerminalTrueColorFormatter())<br>    return sql<br><br>#pretty print sql query from queryset if Psycopg is not installed (or using database other then postgresql)<br># Disadvantage: runs an additional sql query with EXPLAIN<br>def pp_sql_query_any(qs):<br>    from django.db import connections<br>    # Get a cursor tied to the database of queryset<br>    cursor = connections[qs.db].cursor()<br><br>    # Get the query SQL and parameters to be passed into psycopg2<br>    query, params = qs.query.sql_with_params()<br><br>    # Execute the sql<br>    cursor.execute('EXPLAIN ' + query, params)<br><br>    # then get the last executed sql query<br>    sql = str(cursor.db.ops.last_executed_query(cursor, query, params))<br><br>    # Just for confirmation<br>    assert sql.startswith('EXPLAIN ')<br><br>    # Then format it using sqlparser and color it using pygment<br>    import sqlparse<br>    import pygments<br>    from pygments.lexers import SqlLexer<br>    from pygments.formatters import TerminalTrueColorFormatter<br>    # format using sqlparser<br>    sql = sqlparse.format(sql, reindent=True)<br>    # color it using pygments<br>    sql = pygments.highlight(sql,SqlLexer(),TerminalTrueColorFormatter())<br>    return sql<br><br><br>#######################################################<br># Pretty printing traceback format_stack###<br>#######################################################<br><br>def pp_traceback(traceback_format_stack):<br>    import pygments<br>    from pygments.lexers import Python3TracebackLexer<br>    from pygments.formatters import TerminalTrueColorFormatter<br>    traceback_string = ''.join(traceback_format_stack)<br>    traceback_color = pygments.highlight(traceback_string,Python3TracebackLexer(),TerminalTrueColorFormatter(style='trac')) # trac or rainbow_dash<br>    return traceback_color<br></td></tr></tbody></table>

     * ### \[code\] Usage in the python shell\_plus or jupyter as follows

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>Eg:<br>user_set = User.objects.all()<br>from basic_dango import settings<br>import logging<br>logger_custom_string = logging.getLogger("custom_string")<br>from basic_django import settings<br>#logger_custom_string.debug(settings.pp_odir(locals()))<br>#usage:<br>##logger_custom_string.debug(settings.pp_odir(user_set))  # This will pretty print all the properties from dir(user_set)<br>#sql = str(user_set.query)<br>#sql = user_set.query.__str__()<br>##logger_custom_string.debug(settings.pp_sql_sql(sql)) # pretty print the sql obtained from the .query<br>##logger_custom_string.debug(settings.pp_sql_query_pg(user_set)) # pretty print the sql using mogrify only possible with Psycopg<br>##logger_custom_string.debug(settings.pp_sql_query_any(user_set)) # pretty print the sql using EXPLAIN. But runs extra sql<br>#import traceback<br>##logger_custom_string.debug(settings.pp_traceback(traceback.format_stack())) #test traceback<br><br></td></tr></tbody></table>

     * ### \[images\] Custom pretty functions and its usage

       * ![](images/image43.png)![](images/image195.png)![](images/image183.png)![](images/image134.png)![](images/image68.png)![](images/image135.png)

     * ### \[image\] example output of pp\_odir(obj)

       * ![](images/image81.png)

     * ### \[image\] example of pp\_sql\_sql(sql), pp\_sql\_query\_pg(user\_set), pp\_sql\_query\_any(user\_set)

       * ![](images/image58.png)![](images/image214.png)![](images/image150.png)![](images/image125.png)![](images/image84.png)![](images/image104.png)

 * ## Install Django-extensions in dev server:

     * ### \[code\] installation

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>gauranga<br>$ pipenv install django-extensions --dev<br></td></tr></tbody></table>

     * ### \[code\] Add into settings.py

       * You will need to add the django\_extensions application to the INSTALLED\_APPS setting of your Django project settings.py file.:

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>INSTALLED_APPS = (<br>    ...<br>  )<br><br>if DEBUG: <br>     INSTALLED_APPS += [  'django_extensions']<br></td></tr></tbody></table>

     * ### \[images\] settings.py: adding django\_extensions

       * ![](images/image163.png)

       * This will make sure that Django finds the additional management commands provided by django-extensions.

       * The next time you invoke ./manage.py help you should be able to see all the newly available commands.

     * ### \[code\] Some uses of django-extensions

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>python manage.py show_urls<br>#Produce a tab-separated list of (url_pattern, view_function, name) tuples for a project:<br><br>python manage.py shell_plus<br>#Run the enhanced django shell:<br><br>python manage.py runserver_plus<br>#Run the enhanced django runserver, (requires Werkzeug install):<br><br>python manage.py graph_models -a -o myapp_models.png<br>#Generate (and view) a graphviz graph of app models:<br><br>python manage.py passwd username<br>#change password of a username. In dev we forgot passwords<br><br>python manage.py generate_secret_key<br>#generates secret key<br><br>Django-extensions has TitleSlugDescriptionModel, TimeStampedModel which can be inhereted<br><br>Eg:<br>from django.db import models<br>from django_extensions.db.models import (TitleSlugDescriptionModel, TimeStampedModel)<br>class Task(TitleSlugDescriptionModel, TimeStampedModel):<br>          Other fields.<br><br></td></tr></tbody></table>

 * ## Install ipython in dev server:

     * A powerful interactive shell and also A kernel for Jupyter. Also Prints sql

     * ### \[code\] installation of shell\_plus

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>pipenv install ipython --dev<br><br>python manage.py shell_plus --ipython --print-sql<br></td></tr></tbody></table>

 * ## Install jupyter notebook in dev server:

     * IPython introduced a new tool named the Notebook. Inspired by scientific programs like Mathematica or Sage, the Notebook offers a modern and powerful web interface to Python.

     * IPython and Jupyter are great interfaces to the Python language. If you're learning Python, using the IPython terminal or the Jupyter Notebook is highly recommended.

     * ### \[code\] installation of jupyter

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>pipenv install jupyter --dev<br><br>python manage.py shell_plus --notebook<br></td></tr></tbody></table>

     * ### Modify .gitignore

       * Modify the .gitignore to not commit jupyter files (this is already added in .gitignore) but just for reference

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td># IPython<br>*/.ipynb_checkpoints/*.ipynb<br>*.ipynb<br></td></tr></tbody></table>

     * ### \[code\] How to view formatted sql and dicts in jupyter

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>#import the essentials<br>from basic_django import settings<br>import logging<br>logger_database = logging.getLogger("django.db.backends") # this is for sql printing<br>logger_database.filters[0].open() # open the sql printing<br>user_set=User.objects.all()<br>print(user_set) # to see sql do this<br># special case only in jupyter when trying to print query_set.<br># pprint user_set: you have to close() and open() because pp_odir uses `getattr(obj, k)` it will execute everytime the sql. But this does not happen in the views.py<br>logger_database.filters[0].close()<br>print(settings.pp_odir(user_set)) <br>logger_database.filters[0].open()<br><br># here we dont have to open and close<br>print(settings.pp_odir(user_set.__dict__)) <br><br>#without comments:<br><br>from basic_django import settings<br>import logging<br>logger_database = logging.getLogger("django.db.backends") # this is for sql printing<br>logger_database.filters[0].open() # open the sql printing<br>user_set=User.objects.all()<br>print(user_set) # to see sql do this<br>print(settings.pp_odir(user_set))<br></td></tr></tbody></table>

 * ## 

     * ### \[code\] Some interesting observations in jupyter:

       * The below will not the print the sql

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>from basic_django import settings<br>import logging<br>logger_database = logging.getLogger("django.db.backends") # this is for sql printing<br>logger_database.filters[0].open() # open the sql printing<br>User.objects.all()<br>print("Hare Krishna")<br></td></tr></tbody></table>

       * Whereas the below will print

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>from basic_django import settings<br>import logging<br>logger_database = logging.getLogger("django.db.backends") # this is for sql printing<br>logger_database.filters[0].open() # open the sql printing<br>User.objects.all()<br></td></tr></tbody></table>

       * So use user\_set = User.objects.all() and print(user\_set) if we have more code.

 * ## Install runserver\_plus and werkzeug in dev server:

     * Runserver\_plus: Django-extensions includes a management command (runserver\_plus) to start the Werkzeug interactive debugger with your project

     * Werkzeug: Werkzeug is a WSGI utility library for Python. Beyond others, it includes an interactive debugger - what this means is that when your python application throws an exception, Werkzeug will display the exception stacktrace in the browser (that’s not a big deal) and allow you to write python commands interactively wherever you want in that stacktrace (that’s the important stuff).

     * Now, the even more important stuff is that you can abuse the above feature by adding code that will throw an exception in various parts of your application and, as a result get an interactive python prompt at specific parts of your application (for example, before validating your form, or when a method in your model is executed). All this, without the need to use a specific IDE to add breakpoints\!

     * ### \[code\] installation of werkzeug

       * We have already installed django-extensions. So Install werkzeug

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>pipenv install werkzeug --dev<br><br>python manage.py runserver_plus<br><br>(venv) C:\progr\py\werkzeug\testdebug&gt;python manage.py runserver_plus<br> * Restarting with stat<br>Performing system checks...<br><br>System check identified no issues (0 silenced).<br><br>Django version 1.9.7, using settings 'testdebug.settings'<br>Development server is running at http://127.0.0.1:8000/<br>Using the Werkzeug debugger (http://werkzeug.pocoo.org/)<br>Quit the server with CTRL-BREAK.<br> * Debugger is active!<br> * Debugger pin code: 143-738-172<br> * Debugger is active!<br> * Debugger pin code: 174-740-467<br> * Running on http://127.0.0.1:8000/ (Press CTRL+C to quit)<br></td></tr></tbody></table>

       * #### Turn off debugger pin:

         * Now, the “debugger pin” you see is a way to protect your interactive debugger (i.e it asks for the pin before allowing you to enter the interactive prompt). Since this feature should only be used in your local development system I recommend to just disable it by setting the WERKZEUG\_DEBUG\_PIN environment variable to off

       * #### Never Use with production

         * Please be careful with the interactive debugger and never, ever use it in a production deployment even with the debug pin enabled. I also recommend to use it only on a local development server (i.e the server must be run on 127.0.0.1/local IP and not allow remote connections).

       * #### Usage:

         * Now its time for the magic: Let’s add a django view that throws an exception, like this:

         * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>def test(request):<br>    a+=1<br></td></tr></tbody></table>

         * to your urls.py ( url(r'^test/', test ) ) and after you visit test you should see something like this:

       * #### \[image\] using of runserver\_plus

         * ![](images/image169.png)

       * #### \[theory\] how to use

         * Since a variable was not defined you’ll get an exception when you try to increaseit. Now, notice the console icon in the lower right corner - when you click it you’ll get the interactive debugger\! Now you can enter python commands exactly where the a+=1 code was. For example, you can see what are the attributes of the request object you receive (for example, just enter request.GET to output the GET dictionary to the interactive console).

         * Notice that you can get interactive consoles wherever you want in the stacktrace, i.e I could get a console at line 147 of django.core.handlers.base module on the get\_response method — this is needed sometimes especially when you want to see how your code is called by other modules.

         * Refer: how to debug:

         * https://spapas.github.io/2016/06/07/django-werkzeug-debugger/

 * ## 

 * ## Install graph\_models  and pydotplus to generate UML class diagrams from django models

     * To visualize and better understand a project structure we can create UML class diagrams from Django models.

     * We will use a special command for this task included in the django-extensions package called: graph\_models

     * Graph\_models: comes with django-extensions

     * ### \[code\] We have already installed django-extensions. So install pydotplus

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>pipenv install pydotplus --dev<br><br>cd basic_django (where manage.py is located)<br>mkdir project_visualization<br> <br>Then create an image and pdf file<br><br>For image:<br>$ python manage.py graph_models --arrow-shape normal -a -g -o ./project_visualization/my_project_visualized.png<br><br>For pdf:<br>$ python manage.py graph_models --arrow-shape normal -a -g &gt; ./project_visualization/my_project_visualized.dot<br>$ dot -Tpdf ./project_visualization/my_project_visualized.dot &gt; ./project_visualization/my_project_visualized.pdf<br><br>python manage.py graph_models -a -o myapp_models.png<br><br>#Or grouped by application (-o):<br>python manage.py graph_models -a -g -o my_project_visualized.png<br><br># Create a dot file for only the 'foo' and 'bar' applications of your project<br>./manage.py graph_models foo bar &gt; my_project.dot<br><br># Create a graph for only certain models<br>python manage.py graph_models -a -I Foo,Bar -o my_project_subsystem.png<br><br># Create a graph excluding certain models<br>$ ./manage.py graph_models -a -X Foo,Bar -o my_project_sans_foo_bar.png<br><br># Create a graph without showing its edges' labels<br>$ ./manage.py graph_models -a --hide-edge-labels -o my_project_sans_foo_bar.png<br><br># Create a graph with 'normal' arrow shape for relations<br>$ ./manage.py graph_models -a --arrow-shape normal -o my_project_sans_foo_bar_arrow.png<br></td></tr></tbody></table>

       * Refer: https://simpleit.rocks/python/django/generate-uml-class-diagrams-from-django-models/

 * ## Install django-querycount to know the number of queries:

     * [https://github.com/bradmontgomery/django-querycount](https://www.google.com/url?q=https://github.com/bradmontgomery/django-querycount&sa=D&ust=1571383144239000)

     * so we want to know more details of the of total number of queries, duplicate queries etc.

     * Django-querycount provides a middleware to show SQL query count and show duplicate queries on console.

     * ### \[code\] installation and set up

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>pipenv install django-querycount --dev<br><br>Since we are going to edit the source code we will copy the package from site_packages to the project directory<br>cp  -R /home/web_dev/django_basic_documentation/.venv/lib/python3.7/site-packages/querycount /home/web_dev/django_basic_documentation/basic_django/querycount_mod<br><br>Take backup of the middleware.py file since we are going to edit it<br><br>cp /home/web_dev/django_basic_documentation/basic_django/querycount_mod/middleware.py /home/web_dev/django_basic_documentation/basic_django/querycount_mod/middleware_backup.py<br><br>Just add <br><br>if DEBUG:<br>    MIDDLEWARE += [querycount.middleware.QueryCountMiddleware']<br><br>to your MIDDLEWARE<br><br>Notice that django-querycount is hard coded to work only in DEBUG mode set to true so dont have to worry much<br><br>Settings:<br><br>if DEBUG:<br>    QUERYCOUNT = {<br>        'THRESHOLDS': {<br>            'MEDIUM': 50,  ## Color setting: If a query is repeated more than this number then it will be shown in bold brown else light brown<br>            'HIGH': 100,  ## Color setting: If a query is repeated more than this number then it will be shown in red<br>            'MIN_TIME_TO_LOG':0, ## If the total time for query is less than this then it will show<br>            'MIN_QUERY_COUNT_TO_LOG': 0 ## If the total number of queries is less than this then it will show<br>        },<br>        'IGNORE_REQUEST_PATTERNS': [],<br>        'IGNORE_SQL_PATTERNS': [],<br>        'DISPLAY_DUPLICATES': 10000, ## Numer of queries whose sql to be displayed Note: Every query is considered as duplicate even its is executed once. It is considered as repeated as once. We are using 10,000 because we want to see the all the queries<br>        'RESPONSE_HEADER': 'X-DjangoQueryCount-Count'<br>    }<br><br><br><br><br>|------|-----------|----------|----------|----------|------------|<br>| Type | Database  |   Reads  |  Writes  |  Totals  | Duplicates |<br>|------|-----------|----------|----------|----------|------------|<br>| RESP |  default  |    3     |    0     |    3     |     1      |<br>|------|-----------|----------|----------|----------|------------|<br>Total queries: 3 in 1.7738s<br><br><br>Repeated 1 times.<br>SELECT "django_session"."session_key",<br>"django_session"."session_data", "django_session"."expire_date" FROM<br>"django_session" WHERE ("django_session"."session_key" =<br>'dummy_key AND "django_session"."expire_date"<br>&gt; '2018-05-31T09:38:56.369469+00:00'::timestamptz)<br></td></tr></tbody></table>

       * This package provides additional settings to customize output.

     * ### \[code\] Customizing the querycount so that it pretty prints the sql

       * Modify/home/web\_dev/django\_basic\_documentation/basic\_django/querycount\_mod/middleware.py  to pretty print the sql and also print the total time for similar sql to executes

     * ### \[code\] Changes to middleware.py

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td># start added by santhosh<br>from collections import defaultdict<br>def floatdict():<br>    return defaultdict(float)<br># end added by santhosh<br><br><br>            # start added by santhosh<br>            self.queries1 = defaultdict(floatdict)<br>            # end added by santhosh<br><br><br>                    # santhosh added the below two lines so get the total time also<br>                    self.queries1[q['sql']]['count'] += 1<br>                    self.queries1[q['sql']]['time'] += float(q['time'])<br>                    # end added santhosh<br><br><br>    def _duplicate_queries(self, output):<br>        """Appends the most common duplicate queries to the given output."""<br>        if QC_SETTINGS['DISPLAY_DUPLICATES']:<br>            for query, count in self.queries.most_common(QC_SETTINGS['DISPLAY_DUPLICATES']):<br>                lines = '\n[' + format(self.queries1[query]['time']) + ']' + ' Repeated ' + format(count) + ' times.'<br>                lines += "\n" + self._str_query(query) + "\n"<br>                output += self._colorize(lines, count)<br>        return output<br><br>    # santhosh start commented<br>    # def _duplicate_queries(self, output):<br>    #     """Appends the most common duplicate queries to the given output."""<br>    #     if QC_SETTINGS['DISPLAY_DUPLICATES']:<br>    #         for query, count in self.queries.most_common(QC_SETTINGS['DISPLAY_DUPLICATES']):<br>    #             lines = ['\nRepeated {0} times.'.format(count)]<br>    #             lines += wrap(query)<br>    #             lines = "\n".join(lines) + "\n"<br>    #             output += self._colorize(lines, count)<br>    #     return output<br>    # santhosh end commented<br><br>    # Santhosh added<br>    def _str_query(self,sql):<br><br>        # Check if Pygments is available for coloring<br>        try:<br>            import pygments<br>            from pygments.lexers import SqlLexer<br>            from pygments.formatters import TerminalTrueColorFormatter<br>        except ImportError:<br>            pygments = None<br>        # Check if sqlparse is available for indentation<br>        try:<br>            import sqlparse<br>        except ImportError:<br>            sqlparse = None<br>        # Remove leading and trailing whitespaces<br>        if sqlparse:<br>            # Indent the SQL query<br>            sql = sqlparse.format(sql, reindent=True)<br>        if pygments:<br>            # Highlight the SQL query<br>            sql = pygments.highlight(<br>                sql,<br>                SqlLexer(),<br>                #TerminalTrueColorFormatter(style='monokai')<br>                TerminalTrueColorFormatter()<br>            )<br><br>        return sql<br>    # Santhosh ended<br></td></tr></tbody></table>

     * ### \[image\] changes to middleware.py

       * ![](images/image30.png)![](images/image6.png)![](images/image69.png)![](images/image231.png)

     * ### \[code\] Full middleware.py

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>import re<br>import sys<br>import timeit<br>from collections import Counter<br>from textwrap import wrap<br><br>from django.conf import settings<br>from django.db import connections<br>from django.utils import termcolors<br><br>from . qc_settings import QC_SETTINGS<br><br>try:<br>    from django.utils.deprecation import MiddlewareMixin<br>except ImportError:<br>    MiddlewareMixin = object<br><br># start added by santhosh<br>from collections import defaultdict<br>def floatdict():<br>    return defaultdict(float)<br># end added by santhosh<br><br>class QueryCountMiddleware(MiddlewareMixin):<br>    """This middleware prints the number of database queries for each http<br>    request and response. This code is adapted from: http://goo.gl/UUKN0r.<br><br>    NOTE: This middleware is predominately written in the pre-Django 1.10 style,<br>    and uses the MiddlewareMixin for compatibility:<br><br>    https://docs.djangoproject.com/en/1.11/topics/http/middleware/#upgrading-pre-django-1-10-style-middleware<br><br>    """<br><br>    READ_QUERY_REGEX = re.compile("SELECT .*")<br><br>    def __init__(self, *args, **kwargs):<br>        # Call super first, so the MiddlewareMixin's __init__ does its thing.<br>        super(QueryCountMiddleware, self).__init__(*args, **kwargs)<br><br>        if settings.DEBUG:<br>            self.request_path = None<br>            self.stats = {"request": {}, "response": {}}<br>            self.dbs = [c.alias for c in connections.all()]<br>            self.queries = Counter()<br>            # start added by santhosh<br>            from collections import defaultdict<br>            self.queries1 = defaultdict(floatdict)<br>            # end added by santhosh<br>            self._reset_stats()<br><br>            self._start_time = None<br>            self._end_time = None<br>            self.host = None  # The HTTP_HOST pulled from the request<br><br>            # colorizing methods<br>            self.white = termcolors.make_style(opts=('bold',), fg='white')<br>            self.red = termcolors.make_style(opts=('bold',), fg='red')<br>            self.yellow = termcolors.make_style(opts=('bold',), fg='yellow')<br>            self.green = termcolors.make_style(fg='green')<br><br>            # query type detection regex<br>            # TODO: make stats classification regex more robust<br>            self.threshold = QC_SETTINGS['THRESHOLDS']<br><br>    def _reset_stats(self):<br>        self.stats = {"request": {}, "response": {}}<br>        for alias in self.dbs:<br>            self.stats["request"][alias] = {'writes': 0, 'reads': 0, 'total': 0}<br>            self.stats["response"][alias] = {'writes': 0, 'reads': 0, 'total': 0}<br>        self.queries = Counter()<br><br>    def _count_queries(self, which):<br>        for c in connections.all():<br>            for q in c.queries:<br>                if not self._ignore_sql(q):<br>                    if q.get('sql') and self.READ_QUERY_REGEX.search(q['sql']) is not None:<br>                        self.stats[which][c.alias]['reads'] += 1<br>                    else:<br>                        self.stats[which][c.alias]['writes'] += 1<br>                    self.stats[which][c.alias]['total'] += 1<br>                    self.queries[q['sql']] += 1<br><br>                    # santhosh added the below two lines so get the total time also<br>                    self.queries1[q['sql']]['count'] += 1<br>                    self.queries1[q['sql']]['time'] += float(q['time'])<br>                    # end added santhosh<br><br>            # We'll show the worst offender; i.e. the query with the most duplicates<br>            duplicates = self.queries.most_common(1)<br>            if duplicates:<br>                sql, count = duplicates[0]<br>                self.stats[which][c.alias]['duplicates'] = count<br>            else:<br>                self.stats[which][c.alias]['duplicates'] = 0<br><br>    def _ignore_request(self, path):<br>        """Check to see if we should ignore the request."""<br>        return any([<br>            re.match(pattern, path) for pattern in QC_SETTINGS['IGNORE_REQUEST_PATTERNS']<br>        ])<br><br>    def _ignore_sql(self, query):<br>        """Check to see if we should ignore the sql query."""<br>        return any([<br>            re.search(pattern, query.get('sql')) for pattern in QC_SETTINGS['IGNORE_SQL_PATTERNS']<br>        ])<br><br>    def process_request(self, request):<br>        if settings.DEBUG and not self._ignore_request(request.path):<br>            self.host = request.META.get('HTTP_HOST', None)<br>            self.request_path = request.path<br>            self._start_time = timeit.default_timer()<br>            self._count_queries("request")<br><br>    def process_response(self, request, response):<br>        if settings.DEBUG and not self._ignore_request(request.path):<br>            self.request_path = request.path<br>            self._end_time = timeit.default_timer()<br>            self._count_queries("response")<br><br>            # Add query count header, if enabled<br>            if QC_SETTINGS['RESPONSE_HEADER'] is not None:<br>                response[QC_SETTINGS['RESPONSE_HEADER']] = self._calculate_num_queries()<br><br>            self.print_num_queries()<br>            self._reset_stats()<br><br>        return response<br><br>    def _stats_table(self, which, path='', output=None):<br>        if output is None:<br>            if self.host:<br>                host_string = 'http://{0}{1}'.format(self.host, self.request_path)<br>            else:<br>                host_string = self.request_path<br>            output = self.white('\n{0}\n'.format(host_string))<br>            output += "|------|-----------|----------|----------|----------|------------|\n"<br>            output += "| Type | Database  |   Reads  |  Writes  |  Totals  | Duplicates |\n"<br>            output += "|------|-----------|----------|----------|----------|------------|\n"<br><br>        for db, stats in self.stats[which].items():<br>            if stats['total'] &gt; 0:<br>                line = "|{w}|{db}|{reads}|{writes}|{total}|{duplicates}|\n".format(<br>                    w=which.upper()[:4].center(6),<br>                    db=db.center(11),<br>                    reads=str(stats['reads']).center(10),<br>                    writes=str(stats['writes']).center(10),<br>                    total=str(stats['total']).center(10),<br>                    duplicates=str(stats['duplicates']).center(12)<br>                )<br>                output += self._colorize(line, stats['total'])<br>                output += "|------|-----------|----------|----------|----------|------------|\n"<br>        return output<br><br>    def _duplicate_queries(self, output):<br>        """Appends the most common duplicate queries to the given output."""<br>        if QC_SETTINGS['DISPLAY_DUPLICATES']:<br>            for query, count in self.queries.most_common(QC_SETTINGS['DISPLAY_DUPLICATES']):<br>                lines = '\n[' + format(self.queries1[query]['time']) + ']' + ' Repeated ' + format(count) + ' times.'<br>                lines += "\n" + self._str_query(query) + "\n"<br>                output += self._colorize(lines, count)<br>        return output<br><br><br>    # def _duplicate_queries(self, output):<br>    #     """Appends the most common duplicate queries to the given output."""<br>    #     if QC_SETTINGS['DISPLAY_DUPLICATES']:<br>    #         for query, count in self.queries.most_common(QC_SETTINGS['DISPLAY_DUPLICATES']):<br>    #             lines = ['\nRepeated {0} times.'.format(count)]<br>    #             lines += wrap(query)<br>    #             lines = "\n".join(lines) + "\n"<br>    #             output += self._colorize(lines, count)<br>    #     return output<br><br>    # Santhosh added<br>    def _str_query(self,sql):<br><br>        # Check if Pygments is available for coloring<br>        try:<br>            import pygments<br>            from pygments.lexers import SqlLexer<br>            from pygments.formatters import TerminalTrueColorFormatter<br>        except ImportError:<br>            pygments = None<br>        # Check if sqlparse is available for indentation<br>        try:<br>            import sqlparse<br>        except ImportError:<br>            sqlparse = None<br>        # Remove leading and trailing whitespaces<br>        if sqlparse:<br>            # Indent the SQL query<br>            sql = sqlparse.format(sql, reindent=True)<br>        if pygments:<br>            # Highlight the SQL query<br>            sql = pygments.highlight(<br>                sql,<br>                SqlLexer(),<br>                #TerminalTrueColorFormatter(style='monokai')<br>                TerminalTrueColorFormatter()<br>            )<br><br>        return sql<br>    # Santhosh ended<br><br><br>    def _totals(self, which):<br>        reads = 0<br>        writes = 0<br>        for db, stats in self.stats[which].items():<br>            reads += stats['reads']<br>            writes += stats['writes']<br>        return (reads, writes, reads + writes)<br><br>    def _colorize(self, output, metric):<br>        if metric &gt; self.threshold['HIGH']:<br>            output = self.red(output)<br>        elif metric &gt; self.threshold['MEDIUM']:<br>            output = self.yellow(output)<br>        else:<br>            output = self.green(output)<br>        return output<br><br>    def print_num_queries(self):<br>        # Request data<br>        output = self._stats_table("request")<br><br>        # Response data<br>        output = self._stats_table("response", output=output)<br><br>        # Summary of both<br>        if self._end_time and self._start_time:<br>            elapsed = self._end_time - self._start_time<br>        else:<br>            elapsed = 0<br>        <br>        count = self._calculate_num_queries()<br><br>        sum_output = 'Total queries: {0} in {1:.4f}s \n\n'.format(count, elapsed)<br>        sum_output = self._colorize(sum_output, count)<br>        sum_output = self._duplicate_queries(sum_output)<br><br>        # runserver just prints its output to sys.stderr, so we'll do that too.<br>        if elapsed &gt;= self.threshold['MIN_TIME_TO_LOG'] and count &gt;= self.threshold['MIN_QUERY_COUNT_TO_LOG']:<br>            sys.stderr.write(output)<br>            sys.stderr.write(sum_output)<br><br>    def _calculate_num_queries(self):<br>        """<br>        Calculate the total number of request and response queries.<br>        Used for count header and count table.<br>        """<br>        request_totals = self._totals("request")<br>        response_totals = self._totals("response")<br><br>        return request_totals[2] + response_totals[2]  # sum total queries<br></td></tr></tbody></table>

     * ### \[image\] full middleware.py

       * ![](images/image167.png)![](images/image75.png)![](images/image222.png)![](images/image212.png)![](images/image52.png)![](images/image172.png)![](images/image151.png)![](images/image15.png)

     * ### \[code\] Add to the settings.py for querycount

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>if DEBUG:<br>    QUERYCOUNT = {<br>        'THRESHOLDS': {<br>            'MEDIUM': 50,  ## Color setting: If a query is repeated more than this number then it will be shown in bold brown else light brown<br>            'HIGH': 100,  ## Color setting: If a query is repeated more than this number then it will be shown in red<br>            'MIN_TIME_TO_LOG':0, ## If the total time for query is less than this then it will show<br>            'MIN_QUERY_COUNT_TO_LOG': 0 ## If the total number of queries is less than this then it will show<br>        },<br>        'IGNORE_REQUEST_PATTERNS': [],<br>        'IGNORE_SQL_PATTERNS': [],<br>        'DISPLAY_DUPLICATES': 10000, ## Numer of queries whose sql to be displayed Note: Every query is considered as duplicate even its is executed once. It is considered as repeated as once. We are using 10,000 because we want to see the all the queries<br>        'RESPONSE_HEADER': 'X-DjangoQueryCount-Count'<br>    }<br></td></tr></tbody></table>

     * ### \[image\] add to settings.py querycount customization

       * ![](images/image149.png)

     * ### \[image\] Example output

       * ![](images/image78.png)![](images/image140.png)![](images/image223.png)

 * ## Pudb: Python debugger

     * ### \[code\] Install pudb and use it

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>pipenv install pudb --dev<br /><br>And whereever we want to debug we can use<br><br>import pudb<br>pudb.set_trace()<br><br>Or in single line<br><br>import pudb;pudb.set_trace()<br></td></tr></tbody></table>

     * ### \[image\] pudb

       * ![](images/image164.png)

     * ### keybindings

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>Welcome to PuDB, the Python Urwid debugger.<br>-------------------------------------------<br><br>(This help screen is scrollable. Hit Page Down to see more.)<br><br>Keys:<br>    Ctrl-p - edit preferences<br><br>    n - step over ("next")<br>    s - step into<br>    c - continue<br>    r/f - finish current function<br>    t - run to cursor<br>    e - show traceback [post-mortem or in exception state]<br><br>    H - move to current line (bottom of stack)<br>    u - move up one stack frame<br>    d - move down one stack frame<br><br>    o - show console/output screen<br><br>    b - toggle breakpoint<br><br>    j/k - up/down<br>    Ctrl-u/d - page up/down<br>    h/l - scroll left/right<br>    g/G - start/end<br>    L - show (file/line) location / go to line<br>    / - search<br>    ,/. - search next/previous<br><br>    V - focus variables<br>    S - focus stack<br>    B - focus breakpoint list<br>    C - focus code<br><br>    f1/?/H - show this help screen<br>    q - quit<br><br>    Ctrl-c - when in continue mode, break back to PuDB<br><br>    Ctrl-l - redraw screen<br><br>Shell-related:<br>    ! - open the external shell (configured in the settings)<br>    Ctrl-x - toggle the internal shell focus<br><br>    +/- - grow/shrink inline shell (active in command line history)<br>    _/= - minimize/maximize inline shell (active in command line history)<br><br>    Ctrl-v - insert newline<br>    Ctrl-n/p - browse command line history<br>    Tab - yes, there is (simple) tab completion<br><br>Sidebar-related (active in sidebar):<br>    +/- - grow/shrink sidebar<br>    _/= - minimize/maximize sidebar<br>    [/] - grow/shrink relative size of active sidebar box  <br><br>Keys in variables list:<br>    \/space - expand/collapse<br>    t/r/s/c - show type/repr/str/custom for this variable<br>    h - toggle highlighting<br>    @ - toggle repetition at top<br>    * - cycle attribute visibility: public/_private/__dunder__<br>    m - toggle method visibility<br>    w - toggle line wrapping<br>    n/insert - add new watch expression<br>    enter - edit options (also to delete)  <br><br>Keys in stack list:<br><br>    enter - jump to frame<br><br>Keys in breakpoints view:<br><br>    enter - edit breakpoint<br>    d - delete breakpoint<br>    e - enable/disable breakpoint<br><br></td></tr></tbody></table>

       * Tips:

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>Change the theme. Go to ctrl + p (select the theme)<br>Change external python interpreter as ipython: Go to ctrl + p  and change<br></td></tr></tbody></table>

 * ## Logging instead of using printing when level = DEBUG

     * Read “Understanding logging in Python” in MISCELLENEOUS section

     * Main purpose of using logger is to avoid using print statements. And advantage is we can use levels to log only in debug mode.

     * Aim: 

     * 1.  We want to log the sql - we use django’s logger  “django.db.backends”

     * Note: if DEBUG = True, then all of your queries are logged else not. So logging “django.db.backends”. Shows sql only when DEBUG = True, its inbuilt.

     * 2.  We want to log any string - we create on own logger

     * Logger is identified by a name, then LEVEL, handler, filters

     * We can customize the logging by formatter and handlers

     * ### \[code\] Add the following to settings.py. 

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>#######################################################<br># Logging sql and strings<br>#######################################################<br><br>import logging<br><br># Verbose formatter to be used for the handler used in logging "custom_string"<br>class VerFormatter(logging.Formatter):<br>    def format(self, record):<br>        #create a list of all the linenumber: lines <br>        lines=[]<br>        with open(record.pathname) as src:<br>            for index, line in enumerate(src.readlines(), start=1):<br>                if index == record.lineno:<br>                    lines.append('{:4d}***: {}'.format(index, line))<br>                else:<br>                    lines.append('{:7d}: {}'.format(index, line))<br>        # select +/-3 lines from the current line<br>        start=(record.lineno -1) - 5<br>        end=(record.lineno -1) + 5<br>        if record.lineno == len(lines):<br>            end = record.lineno-1<br>        if end &gt; len(lines)-1:<br>            end = len(lines)-1<br>        if record.lineno -1 == 0:<br>            start = 0<br>        if start &lt; 0:<br>            start = 0<br>        code = ''.join(lines[start:end+1]) #lines[start:length]<br><br>        # colorize the code<br>        import pygments<br>        from pygments.lexers.python import Python3Lexer<br>        from pygments.formatters import TerminalTrueColorFormatter<br>        code = pygments.highlight(<br>            code,<br>            Python3Lexer(),<br>            #TerminalTrueColorFormatter(style='monokai')<br>            TerminalTrueColorFormatter()<br>        )<br><br>        #add new attributes<br>        record.codelines = code<br>        record.topline = "--------------------------------------------------------------------------------------------------------------"<br>        record.botline = "--------------------------------------------------------------------------------------------------------------"<br>        return super(VerFormatter, self).format(record)<br><br><br># SQL formatter to be used for the handler used in logging "django.db.backends"<br>class SQLFormatter(logging.Formatter):<br>    def format(self, record):<br><br>        # Check if Pygments is available for coloring <br>        try:<br>            import pygments<br>            from pygments.lexers import SqlLexer<br>            from pygments.formatters import TerminalTrueColorFormatter<br>        except ImportError:<br>            pygments = None<br><br>        # Check if sqlparse is available for indentation<br>        try:<br>            import sqlparse<br>        except ImportError:<br>            sqlparse = None<br><br>        # Remove leading and trailing whitespaces<br>        sql = record.sql.strip()<br><br>        if sqlparse:<br>            # Indent the SQL query<br>            sql = sqlparse.format(sql, reindent=True)<br><br>        if pygments:<br>            # Highlight the SQL query<br>            sql = pygments.highlight(<br>                sql,<br>                SqlLexer(),<br>                #TerminalTrueColorFormatter(style='monokai')<br>                TerminalTrueColorFormatter()<br>            )<br><br>        # Set the record's statement to the formatted query<br>        record.statement = sql<br>        return super(SQLFormatter, self).format(record)<br><br><br><br><br># Filter class to stop or start logging for "django.db.backends"<br>class LoggerGate:<br>    def __init__(self, state='closed'):<br>        # We found that the settings.py runs twice and the filters are created twice. So we have to keep only one. So we delete all the previous filters before we create the new one<br>        import logging<br>        logger_database = logging.getLogger("django.db.backends")<br>        try:<br>            for filter in logger_database.filters:<br>                logger_database.removeFilter(filter)<br>        except Exception as e:<br>            pass<br>        self.state = state<br><br>    def open(self):<br>        self.state = 'open'<br><br>    def close(self):<br>        self.state = 'closed'<br><br>    def filter(self, record):<br>        """<br>        Determine if the specified record is to be logged.<br><br>        Is the specified record to be logged? Returns 0/False for no, nonzero/True for<br>        yes. If deemed appropriate, the record may be modified in-place.<br>        """<br>        return self.state == 'open'<br><br>LOGGING = {<br>    'version': 1,<br>    'disable_existing_loggers': False,<br>    'formatters': {<br>        'sql': {<br>            '()': SQLFormatter,<br>            'format': '[%(duration).3f] %(statement)s',<br>        },<br>        'verbose': {<br>            '()': VerFormatter,<br>            'format': '%(topline)s\n%(asctime)s\nXXX%(levelname)sXXX %(funcName)s() %(pathname)s[:%(lineno)s] %(name)s \n%(topline)s\n%(codelines)s \n%(message)s\n',<br>            #'datefmt': "[%d/%b/%Y %H:%M:%S %p %Z]"<br>        }<br>    },<br>    'handlers': {<br>        'console': {<br>            'level': 'DEBUG',<br>            'formatter': 'verbose',<br>            'class': 'logging.StreamHandler',<br>        },<br>        'sql': {<br>            'class': 'logging.StreamHandler',<br>            'formatter': 'sql',<br>            'level': 'DEBUG',<br>        }<br>    },<br>    'filters': {<br>        'myfilter': {<br>            '()': LoggerGate,<br>        }<br>    },<br>    'loggers': {<br>        'django.db.backends': {<br>            'handlers': ['sql'],<br>            'level': 'DEBUG',<br>            'propagate': False,<br>            'filters': ['myfilter']<br>        },<br>        'django.db.backends.schema': {<br>            'handlers': ['console'],<br>            'level': 'DEBUG',<br>            'propagate': False,<br>        },<br>        'custom_string': {<br>            'level': 'DEBUG' if DEBUG else 'INFO',<br>            'handlers': ['console'],<br>            'propagate': False,<br>        }<br>    }<br>}<br><br></td></tr></tbody></table>

     * ### \[theory\] The problem with django.db.backends

       * Note for “django.db.backends” we use a formatter class to its handler  and also a filter class. The purpose of filter class is to allow start and stop 

       * The problem with django.db.backends.  is that it will log all the sqls. I want to log only sqls in a particular section of a code or where ever i want to see the sqls. We use the filter.

     * ### \[image\] output of logger\_custom\_string.debug("Any String") will show which line number and the some code around it

       * ![](images/image28.png)

     * ### \[image\] settings.py with logging customization

       * ![](images/image90.png)![](images/image160.png)![](images/image200.png)![](images/image105.png)![](images/image77.png)![](images/image8.png)

 * ## Traceback: How to print well formatted traceback at any point in the code

     * ### \[code\] Add the following code to settings.py

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>#######################################################<br># Pretty printing traceback format_stack###<br>#######################################################<br><br>def pp_traceback(traceback_format_stack):<br>    import pygments<br>    from pygments.lexers import Python3TracebackLexer<br>    from pygments.formatters import TerminalTrueColorFormatter<br>    traceback_string = ''.join(traceback_format_stack)<br>    traceback_color = pygments.highlight(traceback_string,Python3TracebackLexer(),TerminalTrueColorFormatter(style='trac')) # trac or rainbow_dash<br>    return traceback_color<br></td></tr></tbody></table>

     * ### \[image\] tracebacl pretty print code

       * ![](images/image203.png)

     * ### \[code\] And use it as following

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>from basic_django import settings<br>import traceback<br>logger_custom_string.debug(settings.pp_traceback(traceback.format_stack())) #test traceback<br><br></td></tr></tbody></table>

 * ## Example view to show usage of pretty pritining logging

     * Example usage view.py (here we are using User, since we havent done any migrations, it will not work, but once the migrations are don then this can be used). Just for reference

     * ### \[code\] basic\_django/views.py

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>import logging<br>logger_custom_string = logging.getLogger("'custom_string'")<br>logger_database = logging.getLogger("django.db.backends")<br><br>def test1(request):<br><br><br>    logger_database.filters[0].open()<br>    #Will allow priting of sql satatements from here<br><br>    from django import db<br>    user_set = User.objects.all()<br><br>    for user in user_set: # Here sql is executed and is printed to console<br>        pass<br>    #Will stop priting of sql satatements after this<br>    logger_database.filters[0].close()<br><br>    from django import db<br>    user_set = User.objects.all()<br><br>    for user in user_set:  # Here sql is executed and is not printed to console<br>        pass<br><br>    now = datetime.datetime.now()<br><br>    logger_custom_string.debug(“testing”)<br><br>    html = "&lt;html&gt;&lt;body&gt;Internal purpose&lt;/body&gt;&lt;/html&gt;"<br>    return HttpResponse(html)<br><br></td></tr></tbody></table>

     * ### \[image\] viewps.py

       * ![](images/image50.png)

 * ## \[code\] Settings.py full

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>"""<br>Django settings for basic_django project.<br><br>Generated by 'django-admin startproject' using Django 2.2.6.<br><br>For more information on this file, see<br>https://docs.djangoproject.com/en/2.2/topics/settings/<br><br>For the full list of settings and their values, see<br>https://docs.djangoproject.com/en/2.2/ref/settings/<br>"""<br><br>import os<br><br># Build paths inside the project like this: os.path.join(BASE_DIR, ...)<br>BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))<br><br><br># Quick-start development settings - unsuitable for production<br># See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/<br><br>#################<br><br>#using .env to store important info and keep single settings.py file and change<br>#the .env variables as per development and production requirements<br><br>#if we use  (e.g env('ALLOWED_HOSTS')) in the settigns.py it has to be mentioned<br>#in .env file even we keep the variable empty in the .env else it will show<br>#error. Thats why we use environ.Env( ALLOWED_HOSTS=(list, ['127.0.0.1:8000']))<br>#to set default value in the settings.py in case its left empty.<br><br>#For accessing env variables from .env inside settings.py <br>#step 1<br>import environ<br><br>#step 2<br># define env as below. Here mention all the defaults we want to have if we leave<br># variables empty in .env file. But this will not check if the variable is<br># defined in .env file or not<br>env = environ.Env(<br>    # set casting, default value<br>    DEBUG=(bool, False),<br>    ALLOWED_HOSTS=(list, ['127.0.0.1:8000']),<br>)<br><br># step 3<br># reading .env file<br>environ.Env.read_env()<br><br>#step 4<br>#getting the env variable value from the KEY. This will check the .env<br>#file for the variable. If its not defined then it will show error. If its empty<br>#and its default is defined then it pics the default value else shows empty. <br>#Eg: SECRET_KEY = env('SECRET_KEY')<br><br>##################<br><br><br># SECURITY WARNING: keep the secret key used in production secret!<br>SECRET_KEY = env('SECRET_KEY')<br><br># SECURITY WARNING: don't run with debug turned on in production!<br>DEBUG = env('DEBUG')<br><br>ALLOWED_HOSTS = env('ALLOWED_HOSTS')<br><br><br># Application definition<br><br>INSTALLED_APPS = [<br>    'django.contrib.admin',<br>    'django.contrib.auth',<br>    'django.contrib.contenttypes',<br>    'django.contrib.sessions',<br>    'django.contrib.messages',<br>    'django.contrib.staticfiles',<br>]<br><br>if DEBUG: <br>     INSTALLED_APPS += [  'django_extensions']<br><br><br>MIDDLEWARE = [<br>    'django.middleware.security.SecurityMiddleware',<br>    'django.contrib.sessions.middleware.SessionMiddleware',<br>    'django.middleware.common.CommonMiddleware',<br>    'django.middleware.csrf.CsrfViewMiddleware',<br>    'django.contrib.auth.middleware.AuthenticationMiddleware',<br>    'django.contrib.messages.middleware.MessageMiddleware',<br>    'django.middleware.clickjacking.XFrameOptionsMiddleware',<br>]<br><br>if DEBUG:<br>    MIDDLEWARE += ['basic_django.querycount.middleware.QueryCountMiddleware']<br><br>if DEBUG:<br>    QUERYCOUNT = {<br>        'THRESHOLDS': {<br>            'MEDIUM': 50,  ## Color setting: If a query is repeated more than this number then it will be shown in bold brown else light brown<br>            'HIGH': 100,  ## Color setting: If a query is repeated more than this number then it will be shown in red<br>            'MIN_TIME_TO_LOG':0, ## If the total time for query is less than this then it will show<br>            'MIN_QUERY_COUNT_TO_LOG': 0 ## If the total number of queries is less than this then it will show<br>        },<br>        'IGNORE_REQUEST_PATTERNS': [],<br>        'IGNORE_SQL_PATTERNS': [],<br>        'DISPLAY_DUPLICATES': 10000, ## Numer of queries whose sql to be displayed Note: Every query is considered as duplicate even its is executed once. It is considered as repeated as once. We are using 10,000 because we want to see the all the queries<br>        'RESPONSE_HEADER': 'X-DjangoQueryCount-Count'<br>    }<br><br><br>ROOT_URLCONF = 'basic_django.urls'<br><br>TEMPLATES = [<br>    {<br>        'BACKEND': 'django.template.backends.django.DjangoTemplates',<br>        'DIRS': [],<br>        'APP_DIRS': True,<br>        'OPTIONS': {<br>            'context_processors': [<br>                'django.template.context_processors.debug',<br>                'django.template.context_processors.request',<br>                'django.contrib.auth.context_processors.auth',<br>                'django.contrib.messages.context_processors.messages',<br>            ],<br>        },<br>    },<br>]<br><br>WSGI_APPLICATION = 'basic_django.wsgi.application'<br><br><br># Database<br># https://docs.djangoproject.com/en/2.2/ref/settings/#databases<br><br>### DATABASES = {<br>###     'default': {<br>###         'ENGINE': 'django.db.backends.sqlite3',<br>###         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),<br>###     }<br>### }<br><br>DATABASES = {<br>    # read os.environ['DATABASE_URL'] and raises ImproperlyConfigured exception if not found<br>    'default': env.db(),  <br>    # env.db() is a short form of env.db(‘DATABASE_URL', default='psql:////tmp/my-tmp-sqlite.db')<br>}<br><br><br><br># Password validation<br># https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators<br><br>AUTH_PASSWORD_VALIDATORS = [<br>    {<br>        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',<br>    },<br>    {<br>        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',<br>    },<br>    {<br>        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',<br>    },<br>    {<br>        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',<br>    },<br>]<br><br><br># Internationalization<br># https://docs.djangoproject.com/en/2.2/topics/i18n/<br><br>LANGUAGE_CODE = 'en-us'<br><br>TIME_ZONE = 'UTC'<br><br>USE_I18N = True<br><br>USE_L10N = True<br><br>USE_TZ = True<br><br><br># Static files (CSS, JavaScript, Images)<br># https://docs.djangoproject.com/en/2.2/howto/static-files/<br><br>STATIC_URL = '/static/'<br><br><br><br><br>#######################################################<br># Logging sql and strings<br>#######################################################<br><br>import logging<br><br># Verbose formatter to be used for the handler used in logging "custom_string"<br>class VerFormatter(logging.Formatter):<br>    def format(self, record):<br>        #create a list of all the linenumber: lines <br>        lines=[]<br>        with open(record.pathname) as src:<br>            for index, line in enumerate(src.readlines(), start=1):<br>                if index == record.lineno:<br>                    lines.append('{:4d}***: {}'.format(index, line))<br>                else:<br>                    lines.append('{:7d}: {}'.format(index, line))<br>        # select +/-3 lines from the current line<br>        start=(record.lineno -1) - 5<br>        end=(record.lineno -1) + 5<br>        if record.lineno == len(lines):<br>            end = record.lineno-1<br>        if end &gt; len(lines)-1:<br>            end = len(lines)-1<br>        if record.lineno -1 == 0:<br>            start = 0<br>        if start &lt; 0:<br>            start = 0<br>        code = ''.join(lines[start:end+1]) #lines[start:length]<br><br>        # colorize the code<br>        import pygments<br>        from pygments.lexers.python import Python3Lexer<br>        from pygments.formatters import TerminalTrueColorFormatter<br>        code = pygments.highlight(<br>            code,<br>            Python3Lexer(),<br>            #TerminalTrueColorFormatter(style='monokai')<br>            TerminalTrueColorFormatter()<br>        )<br><br>        #add new attributes<br>        record.codelines = code<br>        record.topline = "--------------------------------------------------------------------------------------------------------------"<br>        record.botline = "--------------------------------------------------------------------------------------------------------------"<br>        return super(VerFormatter, self).format(record)<br><br><br># SQL formatter to be used for the handler used in logging "django.db.backends"<br>class SQLFormatter(logging.Formatter):<br>    def format(self, record):<br><br>        # Check if Pygments is available for coloring <br>        try:<br>            import pygments<br>            from pygments.lexers import SqlLexer<br>            from pygments.formatters import TerminalTrueColorFormatter<br>        except ImportError:<br>            pygments = None<br><br>        # Check if sqlparse is available for indentation<br>        try:<br>            import sqlparse<br>        except ImportError:<br>            sqlparse = None<br><br>        # Remove leading and trailing whitespaces<br>        sql = record.sql.strip()<br><br>        if sqlparse:<br>            # Indent the SQL query<br>            sql = sqlparse.format(sql, reindent=True)<br><br>        if pygments:<br>            # Highlight the SQL query<br>            sql = pygments.highlight(<br>                sql,<br>                SqlLexer(),<br>                #TerminalTrueColorFormatter(style='monokai')<br>                TerminalTrueColorFormatter()<br>            )<br><br>        # Set the record's statement to the formatted query<br>        record.statement = sql<br>        return super(SQLFormatter, self).format(record)<br><br><br><br><br># Filter class to stop or start logging for "django.db.backends"<br>class LoggerGate:<br>    def __init__(self, state='closed'):<br>        # We found that the settings.py runs twice and the filters are created twice. So we have to keep only one. So we delete all the previous filters before we create the new one<br>        import logging<br>        logger_database = logging.getLogger("django.db.backends")<br>        try:<br>            for filter in logger_database.filters:<br>                logger_database.removeFilter(filter)<br>        except Exception as e:<br>            pass<br>        self.state = state<br><br>    def open(self):<br>        self.state = 'open'<br><br>    def close(self):<br>        self.state = 'closed'<br><br>    def filter(self, record):<br>        """<br>        Determine if the specified record is to be logged.<br><br>        Is the specified record to be logged? Returns 0/False for no, nonzero/True for<br>        yes. If deemed appropriate, the record may be modified in-place.<br>        """<br>        return self.state == 'open'<br><br>LOGGING = {<br>    'version': 1,<br>    'disable_existing_loggers': False,<br>    'formatters': {<br>        'sql': {<br>            '()': SQLFormatter,<br>            'format': '[%(duration).3f] %(statement)s',<br>        },<br>        'verbose': {<br>            '()': VerFormatter,<br>            'format': '%(topline)s\n%(asctime)s\nXXX%(levelname)sXXX %(funcName)s() %(pathname)s[:%(lineno)s] %(name)s \n%(topline)s\n%(codelines)s \n%(message)s\n',<br>            #'datefmt': "[%d/%b/%Y %H:%M:%S %p %Z]"<br>        }<br>    },<br>    'handlers': {<br>        'console': {<br>            'level': 'DEBUG',<br>            'formatter': 'verbose',<br>            'class': 'logging.StreamHandler',<br>        },<br>        'sql': {<br>            'class': 'logging.StreamHandler',<br>            'formatter': 'sql',<br>            'level': 'DEBUG',<br>        }<br>    },<br>    'filters': {<br>        'myfilter': {<br>            '()': LoggerGate,<br>        }<br>    },<br>    'loggers': {<br>        'django.db.backends': {<br>            'handlers': ['sql'],<br>            'level': 'DEBUG',<br>            'propagate': False,<br>            'filters': ['myfilter']<br>        },<br>        'django.db.backends.schema': {<br>            'handlers': ['console'],<br>            'level': 'DEBUG',<br>            'propagate': False,<br>        },<br>        'custom_string': {<br>            'level': 'DEBUG' if DEBUG else 'INFO',<br>            'handlers': ['console'],<br>            'propagate': False,<br>        }<br>    }<br>}<br><br><br>#######################################################<br># Pretty printing object and sql by various means<br>#######################################################<br>#we found that if key is byte string then json.dumps will throw error So we have to convert the dict<br># recursive key as string conversion for byte keys<br>#https://stackoverflow.com/a/57014404/2897115<br><br>## '_preconf_set_by_auto': {'result_backend', 'broker_url'}<br>## the above will raise error: AttributeError: 'str' object has no attribute 'items'<br>## list = [1,3,4] To declare a tuple, we use brackets.<br>## tuples = (1, 2, "a") To declare a tuple, we use parentheses.<br>## sets = {1,2,3} declare a set. Use curly braces<br>def keys_string(d):<br>    rval = {}<br>    if not isinstance(d, dict):<br>        if isinstance(d,(tuple,list,set)):<br>            v = [keys_string(x) for x in d]<br>            return v<br>        else:<br>            return d<br>    for k,v in d.items():<br>        if isinstance(k,bytes):<br>            k = k.decode()<br>        if isinstance(v,dict):<br>            v = keys_string(v)<br>        elif isinstance(v,(tuple,list,set)):<br>            v = [keys_string(x) for x in v]<br>        rval[k] = v<br>    return rval<br><br>def json_dumps_default(obj):<br>    repr_obj = repr(obj)<br>    str_obj = str(obj)<br><br>    if repr_obj == str_obj:<br>        return repr_obj<br>    else:<br>        return repr_obj,f"STR: {str_obj}"<br><br># get_object: pretty print using dir(obj) and then its properties<br>def pp_odir_getobject(obj):<br>    if isinstance(obj,dict):<br>        return keys_string(obj)<br>    if isinstance(obj,(tuple,list,set)):<br>        return keys_string(obj)<br><br>    #c_dict = {k: getattr(obj, k) for k in dir(obj)} # this gives all the properties listed using dir(c)<br><br>    # we are not using the above is because if there are except it stops<br>    c_dict = {<br>                '00_METHODS********************************************************************************':{},<br>                "01_UNDESCORE******************************************************************************":{},<br>                "02_OTHERS*********************************************************************************":{},<br>                "03_EXCEPTIONS*****************************************************************************":{},<br>                }<br>    for key in dir(obj):<br>        try:<br>            attr_obj = getattr(obj, key)<br>            if callable(attr_obj):<br>            #if inspect.ismethod(attr_obj):<br>                c_dict['00_METHODS********************************************************************************'][key] = attr_obj<br>            else:<br>                if key.startswith("_"):<br>                    c_dict['01_UNDESCORE******************************************************************************'][key] = attr_obj<br>                else:<br>                    c_dict['02_OTHERS*********************************************************************************'][key] = attr_obj<br>        except Exception as x:<br>            c_dict['03_EXCEPTIONS*****************************************************************************'][key] = x<br>    return keys_string(c_dict)<br><br><br># pretty print using dir(obj) and then its properties<br>def pp_odir(obj):<br><br>    ##  json.dumps(queryset) in Jupyter runs lot of sqls if the object is query set so we want to avoid that. It work fine with views.py<br>    ## .So we want to stop logging before json_str and continue back with its state after<br>    import logging<br>    logger_database = logging.getLogger("django.db.backends")<br>    try:<br>        log_filt_state=logger_database.filters[0].state<br>        logger_database.filters[0].close()<br>    except:<br>        pass<br><br>    c_dict_flattened = pp_odir_getobject(obj)<br><br>    import json<br>    from pygments import highlight<br>    from pygments.lexers import JsonLexer<br>    from pygments.formatters import TerminalTrueColorFormatter<br>    #Before passing the dict we want to avoid any byte string keys so keys_string(c_dict)<br>    json_str=json.dumps(c_dict_flattened, indent=4, sort_keys=True, default=json_dumps_default)<br><br>    try:<br>        # based on the logging status continue after    <br>        if log_filt_state == 'open':<br>            logger_database.filters[0].open()<br>    except:<br>        pass<br><br>    return highlight(json_str, JsonLexer(), TerminalTrueColorFormatter())<br><br><br># pretty print dictionary<br>def pp_dict(dict):<br>    import json<br>    from pygments import highlight<br>    from pygments.lexers import JsonLexer<br>    from pygments.formatters import TerminalTrueColorFormatter<br>    # json.dumps (needs a dict item and pass default=str to avoid typeError)<br>    json_str=json.dumps(keys_string(dict), indent=4, sort_keys=True, default=json_dumps_default)<br>    return highlight(json_str, JsonLexer(), TerminalTrueColorFormatter())<br><br><br>def pp_sql_sql(sql):<br>    import sqlparse<br>    import pygments<br>    from pygments.lexers import SqlLexer<br>    from pygments.formatters import TerminalTrueColorFormatter<br>    # format using sqlparser<br>    sql = sqlparse.format(sql, reindent=True)<br>    # color it using pygments<br>    sql = pygments.highlight(sql,SqlLexer(),TerminalTrueColorFormatter())<br>    return sql<br><br># pretty print sql query from queryset using mogrify(available only for Psycopg)<br># Advantage: It does not execute any sql to get the sql<br>def pp_sql_query_pg(qs):<br>    from django.db import connections<br>    # Get a cursor tied to the database of queryset<br>    cursor = connections[qs.db].cursor()<br><br>    # Get the query SQL and parameters to be passed into psycopg2<br>    query, params = qs.query.sql_with_params()<br><br>    # use mogrify: Return a query string after arguments binding. The string returned is exactly the one that would be sent to the database running the execute() method or similar.<br>    # mogrify is not a method defined by the Python DB API, but instead an add-on of the Psycopg driver. It does not exist for MySql<br>    sql = cursor.mogrify(query, params)<br><br>    # Then format it using sqlparser and color it using pygment<br>    import sqlparse<br>    import pygments<br>    from pygments.lexers import SqlLexer<br>    from pygments.formatters import TerminalTrueColorFormatter<br>    # format using sqlparser<br>    sql = sqlparse.format(sql, reindent=True)<br>    # color it using pygments<br>    sql = pygments.highlight(sql,SqlLexer(),TerminalTrueColorFormatter())<br>    return sql<br><br>#pretty print sql query from queryset if Psycopg is not installed (or using database other then postgresql)<br># Disadvantage: runs an additional sql query with EXPLAIN<br>def pp_sql_query_any(qs):<br>    from django.db import connections<br>    # Get a cursor tied to the database of queryset<br>    cursor = connections[qs.db].cursor()<br><br>    # Get the query SQL and parameters to be passed into psycopg2<br>    query, params = qs.query.sql_with_params()<br><br>    # Execute the sql<br>    cursor.execute('EXPLAIN ' + query, params)<br><br>    # then get the last executed sql query<br>    sql = str(cursor.db.ops.last_executed_query(cursor, query, params))<br><br>    # Just for confirmation<br>    assert sql.startswith('EXPLAIN ')<br><br>    # Then format it using sqlparser and color it using pygment<br>    import sqlparse<br>    import pygments<br>    from pygments.lexers import SqlLexer<br>    from pygments.formatters import TerminalTrueColorFormatter<br>    # format using sqlparser<br>    sql = sqlparse.format(sql, reindent=True)<br>    # color it using pygments<br>    sql = pygments.highlight(sql,SqlLexer(),TerminalTrueColorFormatter())<br>    return sql<br><br><br>#######################################################<br># Pretty printing traceback format_stack###<br>#######################################################<br><br>def pp_traceback(traceback_format_stack):<br>    import pygments<br>    from pygments.lexers import Python3TracebackLexer<br>    from pygments.formatters import TerminalTrueColorFormatter<br>    traceback_string = ''.join(traceback_format_stack)<br>    traceback_color = pygments.highlight(traceback_string,Python3TracebackLexer(),TerminalTrueColorFormatter(style='trac')) # trac or rainbow_dash<br>    return traceback_color<br></td></tr></tbody></table>

 * ## \[image\] (full settings.py)

     * ![](images/image154.png)![](images/image161.png)![](images/image12.png)![](images/image67.png)![](images/image238.png)![](images/image145.png)![](images/image188.png)![](images/image120.png)![](images/image10.png)![](images/image229.png)![](images/image88.png)![](images/image85.png)![](images/image4.png)![](images/image19.png)![](images/image108.png)![](images/image18.png)![](images/image233.png)![](images/image51.png)![](images/image112.png)

 * ## \[image\] (Settings.py Diff)

     * ![](images/image49.png)![](images/image16.png)![](images/image31.png)![](images/image132.png)![](images/image82.png)![](images/image141.png)![](images/image123.png)![](images/image217.png)![](images/image174.png)![](images/image224.png)![](images/image22.png)![](images/image98.png)![](images/image61.png)![](images/image13.png)![](images/image36.png)![](images/image74.png)![](images/image178.png)![](images/image201.png)![](images/image39.png)

 * ## \[code\] Creating a view to test logging, dict and trceback with pretty printing

     * (We are not doing this now. But after custom\_user and migration it will make sense)

     * Create a file views.py in the 

     * touch ./django\_basic\_documentation/basic\_django/basic\_django/views.py

     * Put the following in the views.py (./django\_basic\_documentation/basic\_django/basic\_django/views.py)

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>from custom_user.models import User<br>from django.http import HttpResponse<br>import datetime<br><br><br>from . import settings<br>from django.db import connections<br>import json<br><br>import logging<br>logger_custom_string = logging.getLogger("custom_string")<br>logger_database = logging.getLogger("django.db.backends")<br><br><br># We are going to test logging, pretty printing and traceback and also querycount<br>def test_7commit(request):<br><br>    logger_database.filters[0].open()<br>    #we allow the database log from here<br><br>    from django import db<br>    user_set = User.objects.all() # here sql is executed and it will be shown in the console<br><br>    for user in user_set:<br>        pass<br><br>    #we block the database log from here<br>    logger_database.filters[0].close()<br><br>    from django import db<br>    user_set = User.objects.all() # here sql is executed and but it will be shown in the console<br><br>    for user in user_set:<br>        pass<br><br>    # checking the functions for pretty priting<br>    logger_custom_string.debug(settings.pp_odir(user_set))  # This will pretty print all the properties from dir(user_set)<br>    logger_custom_string.debug(settings.pp_dict(user_set.__dict__))  # This will pretty print any dictionary<br>    sql = str(user_set.query)<br>    sql = user_set.query.__str__()<br>    logger_custom_string.debug(settings.pp_sql_sql(sql)) # pretty print the sql obtained from the .query<br>    logger_custom_string.debug(settings.pp_sql_query_pg(user_set)) # pretty print the sql using mogrify only possible with Psycopg<br>    logger_custom_string.debug(settings.pp_sql_query_any(user_set)) # pretty print the sql using EXPLAIN. But runs extra sql<br><br><br>    now = datetime.datetime.now()<br>    html = "&lt;html&gt;&lt;body&gt;It is now %s.&lt;/body&gt;&lt;/html&gt;" % now<br>    import traceback<br>    logger_custom_string.debug(settings.pp_traceback(traceback.format_stack())) #test traceback<br>    return HttpResponse(html)<br><br></td></tr></tbody></table>

     * Add the following to the ursl.py (./django\_basic\_documentation/basic\_django/basic\_django/urls.py)

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>from . import views<br><br>path('test7commit',views.test_7commit, name='test_7commit')<br></td></tr></tbody></table>

     * Full ursl.py (./django\_basic\_documentation/basic\_django/basic\_django/urls.py)

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>"""basic_django URL Configuration<br><br>The `urlpatterns` list routes URLs to views. For more information please see:<br>    https://docs.djangoproject.com/en/2.2/topics/http/urls/<br>Examples:<br>Function views<br>    1. Add an import:  from my_app import views<br>    2. Add a URL to urlpatterns:  path('', views.home, name='home')<br>Class-based views<br>    1. Add an import:  from other_app.views import Home<br>    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')<br>Including another URLconf<br>    1. Import the include() function: from django.urls import include, path<br>    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))<br>"""<br>from django.contrib import admin<br>from django.urls import path<br>from . import views<br><br>urlpatterns = [<br>    path('admin/', admin.site.urls),<br>    # this view is for testing 7commit related i.e sql logging, pretty printing, traceback <br>    path('test7commit',views.test_7commit, name='test_7commit')<br><br>]<br></td></tr></tbody></table>

 * ## \[image\] List of Packages installed:

     * ![](images/image107.png)

* # THIRD COMMIT END

* # FOURTH COMMIT START

     * AIM: We want to emails to the users. We will use our gmail email id to send emails. Gmail allows any application to send emails using smtp

 * ## Create an new email without phone verification:

     * Its advised to create a new email id for each project. 

     * Go to create account in gmail

     * Sometimes, even if you enter a phone number, you won’t be able to verify if you used the same phone number on various Gmail or Google accounts. They won’t allow you to proceed further.

     * The below image shows that.

     * ![](images/image129.png)

     * So the how to create a new gmail account without phone verfication

     * ttps://forum.hellboundbloggers.com/t/create-gmail-google-account-without-phone-number-verification/3496

     * In Android phone if we have gmail app we can do it easily without phone verification:

     * Click on the user icon \> Add another account \> Setup email (Google) \> Checking ifno \> Confirm your pin \> Checking info \> in Sing in Form click Create account \> For myself \> Create Google Account (Enter first name and last name) click Next \> then username etc and we are done

 * ## turn on two step verification for this email

     * [https://support.google.com/accounts/answer/185839?co=GENIE.Platform%3DDesktop\&oco=1](https://www.google.com/url?q=https://support.google.com/accounts/answer/185839?co%3DGENIE.Platform%253DDesktop%26oco%3D1&sa=D&ust=1571383144486000)

     * With 2-Step Verification (also known as two-factor authentication), you add an extra layer of security to your account. After you set it up, you’ll sign in to your account in two steps using:

     * Something you know (your password)

     * Something you have (like your phone or a security key dongle)

     * Follow the procedure mentioned

     * For Choose a second verification step -\> we use phone prompt

     * For Set up backups -\> Backup codes (text msg to phone number)

     * Then set up recovery email address and recovery phone number

 * ## Create App password:

     * https://myaccount.google.com/ \> Security \> On the "Signing in to Google" panel, tap 2-Step Verification \> Authenticator app codes

     * Select mail and give a name smtp

     * This will give a 16 digit password

 * ## \[code\] Configure the smtp in Django

     * Add the following to the settings.py

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td># Configuring smtp with gmail account<br>EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'<br>EMAIL_HOST = 'smtp.gmail.com'<br>EMAIL_USE_TLS = True<br>EMAIL_USE_SSL = False<br>EMAIL_PORT = 587<br>EMAIL_HOST_USER = env('EMAIL_HOST_USER')<br>EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')<br><br># Testing mail to which we will send the emails to<br>TESTING_EMAIL=env('TESTING_EMAIL')<br></td></tr></tbody></table>

 * ## \[image\] settings.py email config

     * ![](images/image126.png)

 * ## \[code\] .env file 

     * Add the gmail smtp email, app password and reciever email for testing to the .env file. Refer /home/web\_dev/env\_django\_basic\_documentation/.env (for actual values)

     * We have already adding this.

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td># even we keep the variable empty but if its used in the settigns.py (e.g env('ALLOWED_HOSTS')) it has to be mentioned here else it will show error. Thats why we use environ.Env( ALLOWED_HOSTS=(list, ['127.0.0.1:8000'])) to set default value in the settings.py<br># never use comments on the same line eg:<br># EMAIL_HOST_PASSWORD = 'somepass' #enter pass<br># in settings env('EMAIL_HOST_PASSWORD') value is ('somepass' #enter pass). Even (#enter pass) is included. So it does not recognize # as comment. So put comments only on the top or bottom of line<br><br>DEBUG=on<br><br>SECRET_KEY='somesecretkey'<br><br>DATABASE_URL=psql://user:pass@127.0.0.1:5432/dbname<br><br>ALLOWED_HOSTS=<br><br># using gmail to send emails via smtp<br>EMAIL_HOST_USER=someemail@gmail.com'<br># this is app password not the regular gmail password. Before this enable 2 step verfication<br>EMAIL_HOST_PASSWORD='google_mailapp_password'<br><br># used as recipient email in send_email for testing in test_8commit() in django_basic_documentation/basic_django/basic_django/views.py<br>TESTING_EMAIL='reciever@gmail.com'<br></td></tr></tbody></table>

 * ## \[image\] .env file

     * ![](images/image165.png) 

 * ## \[code\] Change the .env.example

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td># even we keep the variable empty but if its used in the settigns.py (e.g env('ALLOWED_HOSTS')) it has to be mentioned here else it will show error. Thats why we use environ.Env( ALLOWED_HOSTS=(list, ['127.0.0.1:8000'])) to set default value in the settings.py<br># never use comments on the same line eg:<br># EMAIL_HOST_PASSWORD = 'somepass' #enter pass<br># in settings env('EMAIL_HOST_PASSWORD') value is ('somepass' #enter pass). Even (#enter pass) is included. So it does not recognize # as comment. So put comments only on the top or bottom of line<br><br>DEBUG=on<br><br>SECRET_KEY='somekey'<br><br>DATABASE_URL=psql://user:pass@127.0.0.1:5432/dbname<br><br>ALLOWED_HOSTS=<br><br># using gmail to send emails via smtp<br>EMAIL_HOST_USER='username@gmail.com'<br># this is app password not the regular gmail password. Before this enable 2 step verfication<br>EMAIL_HOST_PASSWORD='google_mailapp_password'<br><br># used as recipient email in send_email for testing in test_8commit() in django_basic_documentation/basic_django/basic_django/views.py<br>TESTING_EMAIL='reciever@gmail.com'<br></td></tr></tbody></table>

 * ## \[code\] Create a view to send email using send\_email()

     * basic\_django/viewps.py

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>from basic_django import settings<br><br>def test_8commit(request):<br>    subject = 'Thank you for registering to our site'<br>    message = ' it  means a world to us '<br>    email_from = settings.EMAIL_HOST_USER<br>    recipient_list = [settings.TESTING_EMAIL,]<br>    from django.core.mail import send_mail<br>    send_mail( subject, message, email_from, recipient_list )<br>    html = "&lt;html&gt;&lt;body&gt;Email sent&lt;/body&gt;&lt;/html&gt;"<br>    return HttpResponse(html)<br></td></tr></tbody></table>

 * ## \[image\] basic\_django/viewps.py

     * ![](images/image14.png)

 * ## \[code\] Add to the urls.py 

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>from django.contrib import admin<br>from django.urls import path<br>from . import views<br><br>urlpatterns = [<br>    path('admin/', admin.site.urls),<br>    # this view is for testing 8commit related i.e sending email by gmail smtp<br>    path('test8commit',views.test_8commit, name='test_8commit')<br>]<br></td></tr></tbody></table>

 * ## \[image\] urls.py

     * ![](images/image27.png)

 * ## Open the url and check

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>#gauranga<br />http://localhost:8000/test8commit<br></td></tr></tbody></table>

     * Check the email

* # FOURTH COMMIT END

* # FIFTH COMMIT START

 * ## AIM: CELERY AND REDIS

     * We will use celery.py and redis. 

 * ## \[code\] Install redis and start redis server

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>pacman -S redis<br>redis-server<br></td></tr></tbody></table>

     * Then install in virtual env 

     * |                                                     |

     * | --------------------------------------------------- |

     * | pipenv install celery redis |

 * ## \[image\] Pipfile

     * ![](images/image196.png)

 * ## \[code\] create the file celery.py 

     * /home/web\_dev/django\_basic\_documentation/basic\_django/basic\_django/celery.py

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>import os<br>from celery import Celery<br>import django<br><br>import sys<br><br># when we run <br>#celery -A basic_django worker --loglevel=debug<br># it will run this file.<br><br><br>#we have to set the DJANGO_SETTINGS_MODULE so that the when we run <br># celery -A basic_django worker --loglevel=debug, it will look for the env varaible<br># and it will activate the django and then get all the tasks. in all the installed apps.<br>os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'basic_django.settings')<br><br># This we will need for using the logging config defined in settings.py<br># We can use custom logging we created for django here also.<br>from django.conf import settings<br>from django.utils.log import configure_logging<br>configure_logging(settings.LOGGING_CONFIG, settings.LOGGING)<br><br><br>#This defines the celery app instance<br>redis = 'redis://localhost:6379/'<br>app = Celery('basic_django', <br>        broker=redis, <br>        backend=redis<br>        )<br><br>#Celery instance is assign to app variable by convention. Keep your project<br>#simple and #consistent. Celery instance should be named same as project. For<br>#example if project’s name is “gift-catalogue” then app =<br>#Celery('gift-catalogue', broker=redis, backend=redis)<br></td></tr></tbody></table>

 * ## \[image\] celery.py

     * ![](images/image124.png)

 * ## \[code\] \_\_init\_\_.py

     * /home/web\_dev/django\_basic\_documentation/basic\_django/basic\_django/\_\_init\_\_.py

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>from basic_django.celery import app as celery_app<br><br>## __all__ affects how from ... import * works.<br>## import * is to import all symbols that do not begin with an underscore,<br>## It is a list of strings defining what symbols in a module will be exported when from &lt;module&gt; import * is used on the module.<br>__all__ = ['celery_app']<br><br><br></td></tr></tbody></table>

 * ## \[image\] \_\_init\_\_.py

     * ![](images/image230.png)

 * ## \[code\] DEFINE TASKS:

     * Now define tasks using (you can define in the where ever in the INSTALLED\_APPS. But generally we create tasks.py and then create in them. And later import where we want and use them

     * /home/web\_dev/django\_basic\_documentation/basic\_django/basic\_django/tasks.py

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>###############################<br>## LOGGING<br>import logging<br>logger_custom_string = logging.getLogger("custom_string")<br>from basic_django import settings<br>#usage:<br>#logger_custom_string.debug("ANY STRING")<br>#logger_custom_string.debug(settings.pp_odir(user_set))  # This will pretty print all the properties from dir(user_set)<br>#logger_custom_string.debug(settings.pp_dict(user_set.__dict__))  # This will pretty print any dictionary<br>#sql = str(user_set.query)<br>#sql = user_set.query.__str__()<br>#logger_custom_string.debug(settings.pp_sql_sql(sql)) # pretty print the sql obtained from the .query<br>#logger_custom_string.debug(settings.pp_sql_query_pg(user_set)) # pretty print the sql using mogrify only possible with Psycopg<br>#logger_custom_string.debug(settings.pp_sql_query_any(user_set)) # pretty print the sql using EXPLAIN. But runs extra sql<br>logger_database = logging.getLogger("django.db.backends")<br>#usage:<br>#logger_database.filters[0].open()<br>#logger_database.filters[0].close()<br><br><br>#Note tasks can be declared anywhere. It has to lie in the INSTALLED APPS.<br>#os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'basic_django.settings') does the magic<br>#this will help celery to find all the tasks.<br><br>from basic_django import celery_app<br>from django.core.mail import send_mail<br><br>@celery_app.task<br>def send_email_task(recipient_list,subject,message,):<br>    send_mail(subject, message,None,[recipient_list])<br>    logger_custom_string.debug("Email Sent")<br></td></tr></tbody></table>

 * ## \[image\] tasks.py

     * ![](images/image152.png)

 * ## \[code\] views.py

     * /home/web\_dev/django\_basic\_documentation/basic\_django/basic\_django/tasks.py/views.py

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>from .tasks import send_email_task<br><br>def celery_example_5commit(request):<br>    subject = 'Thank you for registering to our site'<br>    message = ' it  means a world to us '<br>    email_from = settings.EMAIL_HOST_USER<br>    recipient_list = [settings.TESTING_EMAIL,]<br>    from django.core.mail import send_mail<br>    # USING CELERY TASK for sending email Asynchronously<br>    #match.email_user(subject, message). This will delay the response <br>    # So will do this task asynchronously using celery<br>    # We have created a celery task. Using it we will send the email.<br>    # The code does not have to wait till the email is sent<br>    send_email_task.delay(email,subject,message)<br>    html = "&lt;html&gt;&lt;body&gt;Email sent using celery&lt;/body&gt;&lt;/html&gt;"<br>    return HttpResponse(html)<br></td></tr></tbody></table>

 * ## \[image\] views.py

     * ![](images/image87.png)

 * ## \[code\] FIRST START REDIS

     * $ redis-server

 * ## \[code\] START CELERY (go into the project where manage.py is there)

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>$ celery -A basic_django worker --loglevel=debug      (Use debug to see what tasks are loaded)                             <br><br> -------------- celery@gauranga v4.3.0 (rhubarb)<br>---- **** ----- <br>--- * ***  * -- Linux-5.0.5-arch1-1-ARCH-x86_64-with-arch-Arch-Linux 2019-10-12 13:16:02<br>-- * - **** --- <br>- ** ---------- [config]<br>- ** ---------- .&gt; app:         basic_django:0x7f760bfa97b8<br>- ** ---------- .&gt; transport:   redis://localhost:6379//<br>- ** ---------- .&gt; results:     redis://localhost:6379/<br>- *** --- * --- .&gt; concurrency: 4 (prefork)<br>-- ******* ---- .&gt; task events: OFF (enable -E to monitor tasks in this worker)<br>--- ***** ----- <br> -------------- [queues]<br>                .&gt; celery           exchange=celery(direct) key=celery<br>                <br><br>[tasks]<br>  . basic_django.tasks.send_email_task<br>  . celery.accumulate<br>  . celery.backend_cleanup<br>  . celery.chain<br>  . celery.chord<br>  . celery.chord_unlock<br>  . celery.chunks<br>  . celery.group<br>  . celery.map<br>  . celery.starmap<br><br></td></tr></tbody></table>

 * ## \[image\] Starting celery

* # ![](images/image71.png)

 * ## NOTE: After modify/add tasks refresh celery

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>#gauranga<br>Note whenever we create a new task or change its location then we have to rerun the celery.<br></td></tr></tbody></table>

 * ## Flower: Real-time Celery web-monitor

     * ### \[code\] install flower and how to use it

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>pipenv install flower --dev<br>celery -A proj flower<br><br>The default port is http://localhost:5555, but you can change this using the –port argument:<br>$ celery -A proj flower --port=5555<br></td></tr></tbody></table>

     * ### \[image\] images

       * ![](images/image207.png)

       * ![](images/image62.png)  

* # FIFTH COMMIT END

* # SIX COMMIT START

 * ## 1.Create a custom\_user application in Django

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>#gauranga<br>python manage.py startapp  custom_user<br></td></tr></tbody></table>

     * ### \[image\] directory tree

       * ![](images/image56.png)

* # SIX COMMIT END

* # SIX\_A COMMIT START

 * ## Add custom\_user to INSTALLED\_APPS  of settings.py

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>INSTALLED_APPS = [<br>    'django.contrib.admin',<br>    'django.contrib.auth',<br>    'django.contrib.contenttypes',<br>    'django.contrib.sessions',<br>    'django.contrib.messages',<br>    'django.contrib.staticfiles',<br>    'custom_user'<br>]<br></td></tr></tbody></table>

 * ##         \[image\] settings.py diff

     *         ![](images/image130.png)

* # SIX\_A COMMIT END

* # SEVENTH COMMIT THEORY START

 * ## Custom User model

     * ### CONCEPTS TO BE UNDERSTOOD BEFORE STARTING WITH CREATING CUSTOM USER MODEL

       * #### 1.AUTH\_USER\_MODEL

         * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td><a href="https://www.google.com/url?q=https://docs.djangoproject.com/en/2.2/ref/settings/%23auth-user-model&amp;sa=D&amp;ust=1571383144548000" class="c24"></a><br>Default: 'auth.User'<br><br>The model to use to represent a User. See <a href="https://www.google.com/url?q=https://docs.djangoproject.com/en/2.2/topics/auth/customizing/%23auth-custom-user&amp;sa=D&amp;ust=1571383144549000" class="c24">Substituting a custom User model</a>.<br><br>Warning<br><br>You cannot change the AUTH_USER_MODEL setting during the lifetime of a project (i.e. once you have made and migrated models that depend on it) without serious effort. It is intended to be set at the project start, and the model it refers to must be available in the first migration of the app that it lives in. See <a href="https://www.google.com/url?q=https://docs.djangoproject.com/en/2.2/topics/auth/customizing/%23auth-custom-user&amp;sa=D&amp;ust=1571383144550000" class="c24">Substituting a custom User model</a> for more details.<br></td></tr></tbody></table>

         * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>some sites it makes more sense to use an email address as your identification token instead of a username.<br><br>If you’re starting a new project, it’s highly recommended to set up a custom user model, even if the default <a href="https://www.google.com/url?q=https://docs.djangoproject.com/en/2.2/ref/contrib/auth/%23django.contrib.auth.models.User&amp;sa=D&amp;ust=1571383144552000" class="c24">User</a> model is sufficient for you. This model behaves identically to the default user model, but you’ll be able to customize it in the future if the need arises:<br><br>Do this before creating any migrations or running manage.py migratefor the first time.<br><br>Django allows you to override the default user model by providing a value for the <a href="https://www.google.com/url?q=https://docs.djangoproject.com/en/2.2/ref/settings/%23std:setting-AUTH_USER_MODEL&amp;sa=D&amp;ust=1571383144553000" class="c24">AUTH_USER_MODEL</a> setting that references a custom model:<br><br>AUTH_USER_MODEL = 'myapp.MyUser'<br>This dotted pair describes the name of the Django app (which must be in your <a href="https://www.google.com/url?q=https://docs.djangoproject.com/en/2.2/ref/settings/%23std:setting-INSTALLED_APPS&amp;sa=D&amp;ust=1571383144555000" class="c24">INSTALLED_APPS</a>), and the name of the Django model that you wish to use as your user model.<br></td></tr></tbody></table>

       * #### 2.Custom model extending AbstractUser

         * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>from django.contrib.auth.models import AbstractUser<br><br>class User(AbstractUser):<br>    pass<br><br>Don’t forget to point <a href="https://www.google.com/url?q=https://docs.djangoproject.com/en/2.2/ref/settings/%23std:setting-AUTH_USER_MODEL&amp;sa=D&amp;ust=1571383144559000" class="c24">AUTH_USER_MODEL</a> to it. Do this before creating any migrations or running manage.py migratefor the first time.<br></td></tr></tbody></table>

       * #### 3.Also, register the model in the app’s admin.py:

         * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>from django.contrib import admin<br>from django.contrib.auth.admin import UserAdmin<br>from .models import User<br><br>admin.site.register(User, UserAdmin)<br></td></tr></tbody></table>

       * #### 4.Model Manager:

         * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>Each model has at least one <a href="https://www.google.com/url?q=https://docs.djangoproject.com/en/2.2/topics/db/managers/%23django.db.models.Manager&amp;sa=D&amp;ust=1571383144564000" class="c24">Manager</a>, and it’s called <a href="https://www.google.com/url?q=https://docs.djangoproject.com/en/2.2/ref/models/class/%23django.db.models.Model.objects&amp;sa=D&amp;ust=1571383144564000" class="c24">objects</a> by default. Access it directly via the model class, like so:<br>&gt;&gt;&gt; Blog.objects<br>&lt;django.db.models.manager.Manager object at ...&gt;<br>&gt;&gt;&gt; b = Blog(name='Foo', tagline='Bar')<br>&gt;&gt;&gt; b.objects<br>Traceback:<br>    ...<br>AttributeError: "Manager isn't accessible via Blog instances."<br><br>Note: <br>Managers are accessible only via model classes, rather than from model instances, to enforce a separation between “table-level” operations and “record-level” operations.<br><br>The <a href="https://www.google.com/url?q=https://docs.djangoproject.com/en/2.2/topics/db/managers/%23django.db.models.Manager&amp;sa=D&amp;ust=1571383144568000" class="c24">Manager</a> is the main source of QuerySets for a model. For example, Blog.objects.all() returns a <a href="https://www.google.com/url?q=https://docs.djangoproject.com/en/2.2/ref/models/querysets/%23django.db.models.query.QuerySet&amp;sa=D&amp;ust=1571383144568000" class="c24">QuerySet</a>that contains all Blog objects in the database.<br></td></tr></tbody></table>

       * #### 5.Manager names

         * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>By default, Django adds a Manager with the name objects to every Django model class. However, if you want to use objects as a field name, or if you want to use a name other than objects for the Manager, you can rename it on a per-model basis. To rename the Manager for a given class, define a class attribute of type models.Manager() on that model. For example:<br><br>from django.db import models<br><br>class Person(models.Model):<br>    #...<br>    people = models.Manager()<br><br>Using this example model, Person.objects will generate an AttributeError exception, but Person.people.all() will provide a list of all Person objects.<br></td></tr></tbody></table>

       * #### 6.Custom managers

         * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>There are two reasons you might want to customize a Manager: <br><ul><li>to add extra Manager methods, </li><li>and/or to modify the initial QuerySet the Manager returns.</li></ul></td></tr></tbody></table>

       * #### 7.Custom User fields (USERNAME\_FIELD, EMAIL\_FIELD, REQUIRED\_FIELDS)

         * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>USERNAME_FIELD<a href="https://www.google.com/url?q=https://docs.djangoproject.com/en/2.2/topics/auth/customizing/%23django.contrib.auth.models.CustomUser.USERNAME_FIELD&amp;sa=D&amp;ust=1571383144575000" class="c24">¶</a><br>A string describing the name of the field on the user model that is used as the unique identifier. This will usually be a username of some kind, but it can also be an email address, or any other unique identifier. The field must be unique (i.e., have unique=True set in its definition), unless you use a custom authentication backend that can support non-unique usernames.<br>In the following example, the field identifier is used as the identifying field:<br>class MyUser(AbstractBaseUser):<br>    identifier = models.CharField(max_length=40, unique=True)<br>    ...<br>    USERNAME_FIELD = 'identifier'<br><br><br>EMAIL_FIELD<a href="https://www.google.com/url?q=https://docs.djangoproject.com/en/2.2/topics/auth/customizing/%23django.contrib.auth.models.CustomUser.EMAIL_FIELD&amp;sa=D&amp;ust=1571383144578000" class="c24">¶</a><br>A string describing the name of the email field on the User model. This value is returned by<a href="https://www.google.com/url?q=https://docs.djangoproject.com/en/2.2/topics/auth/customizing/%23django.contrib.auth.models.AbstractBaseUser.get_email_field_name&amp;sa=D&amp;ust=1571383144579000" class="c24">get_email_field_name()</a>.<br><br>REQUIRED_FIELDS<a href="https://www.google.com/url?q=https://docs.djangoproject.com/en/2.2/topics/auth/customizing/%23django.contrib.auth.models.CustomUser.REQUIRED_FIELDS&amp;sa=D&amp;ust=1571383144580000" class="c24">¶</a><br>A list of the field names that will be prompted for when creating a user via the <a href="https://www.google.com/url?q=https://docs.djangoproject.com/en/2.2/ref/django-admin/%23django-admin-createsuperuser&amp;sa=D&amp;ust=1571383144580000" class="c24">createsuperuser</a> management command. The user will be prompted to supply a value for each of these fields. It must include any field for which <a href="https://www.google.com/url?q=https://docs.djangoproject.com/en/2.2/ref/models/fields/%23django.db.models.Field.blank&amp;sa=D&amp;ust=1571383144581000" class="c24">blank</a> is False or undefined and may include additional fields you want prompted for when a user is created interactively. REQUIRED_FIELDS has no effect in other parts of Django, like creating a user in the admin.<br><br>For example, here is the partial definition for a user model that defines two required fields - a date of birth and height:<br>class MyUser(AbstractBaseUser):<br>    ...<br>    date_of_birth = models.DateField()<br>    height = models.FloatField()<br>    ...<br>    REQUIRED_FIELDS = ['date_of_birth', 'height']<br><br></td></tr></tbody></table>

       * #### Abstract Base Classes

         * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>   class Meta:<br>        abstract = True<br></td></tr></tbody></table>

         * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>Abstract base classes are useful when you want to put some common information into a number of other models. You write your base class and put abstract=True in the <a href="https://www.google.com/url?q=https://docs.djangoproject.com/en/2.2/topics/db/models/%23meta-options&amp;sa=D&amp;ust=1571383144586000" class="c24">Meta</a> class. This model will then not be used to create any database table. Instead, when it is used as a base class for other models, its fields will be added to those of the child class.<br><br>An example:<br>from django.db import models<br><br>class CommonInfo(models.Model):<br>    name = models.CharField(max_length=100)<br>    age = models.PositiveIntegerField()<br><br>    class Meta:<br>        abstract = True<br><br>class Student(CommonInfo):<br>    home_group = models.CharField(max_length=5)<br><br>The Student model will have three fields: name, age and home_group. The CommonInfo model cannot be used as a normal Django model, since it is an abstract base class. It does not generate a database table or have a manager, and cannot be instantiated or saved directly.<br><br>Fields inherited from abstract base classes can be overridden with another field or value, or be removed with None.<br><br>For many uses, this type of model inheritance will be exactly what you want. It provides a way to factor out common information at the Python level, while still only creating one database table per child model at the database level.<br><h4 id="h.pikurthxt6lq" class="c6 c60"></h4>Meta inheritance<a href="https://www.google.com/url?q=https://docs.djangoproject.com/en/2.2/topics/db/models/%23meta-inheritance&amp;sa=D&amp;ust=1571383144593000" class="c24">¶</a><br><a href="https://www.google.com/url?q=https://docs.djangoproject.com/en/2.2/topics/db/models/%23meta-inheritance&amp;sa=D&amp;ust=1571383144594000" class="c24"></a><br>When an abstract base class is created, Django makes any <a href="https://www.google.com/url?q=https://docs.djangoproject.com/en/2.2/topics/db/models/%23meta-options&amp;sa=D&amp;ust=1571383144594000" class="c24">Meta</a> inner class you declared in the base class available as an attribute. If a child class does not declare its own <a href="https://www.google.com/url?q=https://docs.djangoproject.com/en/2.2/topics/db/models/%23meta-options&amp;sa=D&amp;ust=1571383144594000" class="c24">Meta</a> class, it will inherit the parent’s <a href="https://www.google.com/url?q=https://docs.djangoproject.com/en/2.2/topics/db/models/%23meta-options&amp;sa=D&amp;ust=1571383144595000" class="c24">Meta</a>. If the child wants to extend the parent’s <a href="https://www.google.com/url?q=https://docs.djangoproject.com/en/2.2/topics/db/models/%23meta-options&amp;sa=D&amp;ust=1571383144595000" class="c24">Meta</a> class, it can subclass it. For example:<br><br>from django.db import models<br><br>class CommonInfo(models.Model):<br>    # ...<br>    class Meta:<br>        abstract = True<br>        ordering = ['name']<br><br>class Student(CommonInfo):<br>    # ...<br>    class Meta(CommonInfo.Meta):<br>        db_table = 'student_info'<br><br>Django does make one adjustment to the <a href="https://www.google.com/url?q=https://docs.djangoproject.com/en/2.2/topics/db/models/%23meta-options&amp;sa=D&amp;ust=1571383144600000" class="c24">Meta</a> class of an abstract base class: before installing the <a href="https://www.google.com/url?q=https://docs.djangoproject.com/en/2.2/topics/db/models/%23meta-options&amp;sa=D&amp;ust=1571383144600000" class="c24">Meta</a> attribute, it sets abstract=False. This means that children of abstract base classes don’t automatically become abstract classes themselves. Of course, you can make an abstract base class that inherits from another abstract base class. You just need to remember to explicitly set abstract=True each time.<br></td></tr></tbody></table>

       * #### 8.Underscore Prefix

         * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>#gauranga<br>The underscore prefix is meant as a hint to another programmer that a variable or method starting with a single underscore is intended for internal use. This convention is defined in PEP 8. This isn't enforced byPython. Python does not have strong distinctions between “private” and “public” variables like Java does.<br></td></tr></tbody></table>

* # SEVENTH COMMIT THEORY END

* # EIGHT COMMIT START

 * ## AIM OF SIXTH COMMIT - FLowchart for User Auth - Session based

     * We want to create a login, user login, registration, logout, password reset,  email verification by OTP by Session based authentication

 * ## Logic:

     * ### Login Page FLow Chart:

       * ![](images/image221.jpg)

     * ### Create new User and Pass Page Flow Chart:

       * ![](images/image157.jpg)

       * -----

     * ### Otp page for login\_via\_otp:

       * ![](images/image92.jpg)

       * -----

     * ### Reset password:

       * ![](images/image60.jpg)

       * -----

 * ## 

 * ## Making flowcharts using libreoffice draw:

     * We use libreoffice to make the above flowcharts

     * ./django\_basic\_documentation/flowcharts/User\_auth\_session\_based.odg

     * Then we export it as pdf

     * Then convert pdf to images using 

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>#gauranga<br>convert -geometry 1600x1600 -density 200x200 -quality 100 User_auth_session_based.pdf file-%00d.jpg<br></td></tr></tbody></table>

     * Then rename the images according to the subject and insert images in google docs

* # EIGHT COMMIT END

* # NINTH COMMIT START

 * ## \[theory\] Creating Custom user with email as login:

     * We want to use email as the login. And also we want to confirm email by sending an otp to the email address. 

     * Background:

     * The user model is located in /python3.6/site-packages/django/contrib/auth/models.py. So it cannot be changed or modified as per our needs. So inorder to have our custom user model we have to create an app and define a model which inherits the  AbstractUser class

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>If you don't use an abstract base class two tables will be created in the database instead of one.<br><br>Example:<br><br>class MyUser(AuthUser): <br>new fields…<br>This will create two tables AuthUser and MyUser also. Its called <br>Vs<br><br>class MyUser(AbstractBaseUser): ...<br>This will create only one table MyUser<br><br></td></tr></tbody></table>

     * The following will be the models.py for custom user. Read the comments for more explanation

     * Also we have to change the Model Manager so that it accomodates the create\_user function with email

 * ## \[code\] Custom user fields:

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td># Optional fields<br>    about = models.TextField(max_length=500, blank=True)<br>    location = models.CharField(max_length=30, blank=True)<br>    birth_date = models.DateField(null=True, blank=True)<br>    first_name = models.CharField(_('first name'), max_length=30,blank=True)<br>    last_name = models.CharField(_('last name'), max_length=150,blank=True)<br><br># Auto generated<br>    modified_date = models.DateTimeField(_('modified date'),auto_now=True)<br>    creation_date = models.DateTimeField(_('creation date'),auto_now_add=True)<br><br># to be manual set &amp;&amp; compulsory whenever loged in/ created <br>    email = models.EmailField(<br>        _('email address'),<br>        help_text="Please Enter valid Email Address",<br>        unique=True,<br>        error_messages={<br>            'unique': _("This email already exists."),<br>        },<br>    )<br>    is_active = models.BooleanField(<br>        _('active'),<br>        default=False,<br>        help_text=_(<br>            'Designates whether this user should be treated as active. '<br>            'Unselect this instead of deleting accounts.'<br>        )<br>    )<br>    last_login2 = models.DateTimeField(_('last login 2'),blank=True, null=True)<br><br># recent dates<br>    recentdate_login_via_passwd = models.DateTimeField(_('last login via password'), blank=True, null=True)<br>    recentdate_login_via_otp = models.DateTimeField(_('last login via otp'), blank=True, null=True)<br>    recentdate_password_change = models.DateTimeField(_('last password change'), blank=True, null=True)<br><br># OTP related<br>    recent_otp_used_for_pass_change = models.CharField(<br>        _('otp'),<br>        help_text="Please Enter valid OTP sent to your Email",<br>        max_length=6,<br>        validators=[<br>            RegexValidator(<br>                r'^\d{6}$',<br>                message=_('OTP shoud be of 6 digits'),<br>                code='invalid'<br>            )<br>        ]<br>    )<br><br>    date_of_recent_otp_used_for_pass_change = models.DateTimeField(null=True)<br><br>    # when we create a login and pass singup form, we try to verify the email then this is required<br>    otp_used_while_passlogin_create = models.CharField(<br>        _('otp'),<br>        help_text="Please Enter valid OTP sent to your Email",<br>        max_length=6,<br>        validators=[<br>            RegexValidator(<br>                r'^\d{6}$',<br>                message=_('OTP shoud be of 6 digits'),<br>                code='invalid'<br>            )<br>        ]<br>    )<br><br>    date_of_otp_used_while_passlogin_create = models.DateTimeField(null=True)<br><br>    first_otp_used_for_otplogin = models.CharField(<br>        _('otp'),<br>        help_text="Please Enter valid OTP sent to your Email",<br>        max_length=6,<br>        validators=[<br>            RegexValidator(<br>                r'^\d{6}$',<br>                message=_('OTP shoud be of 6 digits'),<br>                code='invalid'<br>            )<br>        ]<br>    )<br><br>    date_of_first_otp_used_for_otplogin = models.DateTimeField(null=True)<br></td></tr></tbody></table>

     * For the code view models.py below

 * ## \[image\] showing the fields of custom\_user

     * ![](images/image23.png)![](images/image185.png)![](images/image184.png)![](images/image45.png)![](images/image234.png)

 * ## Usersessions Log

     * We want to store the following everytime a user logs in via a OTP or pass or changes his email id

 * ## \[code\] list of things to store for every user session

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>User (Foriegn Key)<br>User_email<br>Otp_used_for_pass_change<br>Otp_used_while_passlogin_create<br>Otp_used_for_otplogin<br>Device_type<br>Ip_address<br>Created_time<br>Action_type {pass_change, login_by_otp, login_by_pass, passlogin_email_validation}<br></td></tr></tbody></table>

     * ### \[code\] Ip\_address and settings.py:

       * To get the ip\_address: we will add the followin code in settings.py and use it wherever we want

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>#######################################################<br># Get ip address<br>#######################################################<br><br>def get_client_ip(request):<br>    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')<br>    if x_forwarded_for:<br>        ip = x_forwarded_for.split(',')[0]<br>    else:<br>        ip = request.META.get('REMOTE_ADDR')<br>    return ip<br></td></tr></tbody></table>

     * ### \[image\] ip\_address

       * ![](images/image115.png)

 * ## \[image\] showing the Usersessionlog

     * ![](images/image189.png)![](images/image34.png)![](images/image63.png)

 * ## \[code\] models.py  Full code

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>from django.contrib.auth.models import AbstractUser, BaseUserManager<br>from django.db import models<br>from django.utils.translation import ugettext_lazy as _<br>from django.contrib.auth.hashers import make_password<br>from django.conf import settings<br>from django.db import models<br>from django.utils import timezone<br>from django.core.exceptions import (<br>    FieldDoesNotExist, ImproperlyConfigured, ValidationError,<br>    )<br><br>from django.contrib.auth import password_validation<br>import uuid<br>from django.core.validators  import RegexValidator,MinLengthValidator<br><br><br>###############################<br>## LOGGING<br>import logging<br>logger_custom_string = logging.getLogger("custom_string")<br>from basic_django import settings<br>#usage:<br>#logger_custom_string.debug(settings.pp_odir(user_set))  # This will pretty print all the properties from dir(user_set)<br>#sql = str(user_set.query)<br>#sql = user_set.query.__str__()<br>#logger_custom_string.debug(settings.pp_sql_sql(sql)) # pretty print the sql obtained from the .query<br>#logger_custom_string.debug(settings.pp_sql_query_pg(user_set)) # pretty print the sql using mogrify only possible with Psycopg<br>#logger_custom_string.debug(settings.pp_sql_query_any(user_set)) # pretty print the sql using EXPLAIN. But runs extra sql<br>#import traceback<br>#logger_custom_string.debug(settings.pp_traceback(traceback.format_stack())) #test traceback<br>logger_database = logging.getLogger("django.db.backends")<br>#usage:<br>#logger_database.filters[0].open()<br>#logger_database.filters[0].close()<br><br><br>import string<br>import secrets<br>def generateSecureRandomString(stringLength=20):<br>    """Generate a secure random string of letters, digits and special characters """<br>    password_characters = string.ascii_letters + string.digits + string.punctuation<br>    return ''.join(secrets.choice(password_characters) for i in range(stringLength))<br><br><br><br># We want to use email as the login. The default User Manager () at <br># /venv_btg/lib/python3.6/site-packages/django/contrib/auth/models.py <br># is made for username based so we have to  rewrite to email based<br><br><br>class UserManager(BaseUserManager):<br>    """Define a model manager for User model with no username field."""<br><br>    # You can optionally serialize managers into migrations and have them available in<br>    # RunPython operations. This is done by defining a use_in_migrations attribute on<br>    # the manager class:<br><br>    use_in_migrations = True<br><br>    def _create_user(self, email, password, **extra_fields):<br>        """Create and save a User with the given email and password."""<br>        if not email:<br>            raise ValueError('The given email must be set')<br><br>        # what is normalizing_email<br>        # For email addresses, foo@bar.com and foo@BAR.com are equivalent;<br>        # the domain part is case-insensitive according to the RFC specs.<br>        # Normalizing means providing a canonical representation,<br>        # so that any two equivalent email strings normalize to the same thing.<br>        # The comments on the Django method explain:<br>        # Normalize the email address by lowercasing the domain part of it.<br><br>        email = self.normalize_email(email)<br>        user = self.model(email=email, **extra_fields)<br><br><br>        # What is self.model() in django custom UserManager<br>        <br>        # Well what you define here is a UserManager class. This inherits from<br>        # the BaseUserManager class. This is a subclass of the Manager class.<br>        # You actually use manager all the time. For example SomeModel.objects<br>        # is a manager.<br><br>        # A manager has, if it is used, a reference to the model it manages.<br>        # So SomeModel.objects is a manager, but that manager has an attribute<br>        # .model that actually refers back to the SomeModel class.<br><br>        # In this case your self.model will refer to User model<br><br><br>        # Sets the user’s password to the given raw string, taking care of the password hashing.<br>        # Doesn’t save the User object.<br>        user.set_password(password)<br>        <br>        user.save(using=self._db)<br>        <br>        return user<br><br>        # Q: using model.save() from django shell will not validate the data<br><br>        # Creating an instance of a Model and calling save on that instance<br>        # does not call full_clean. Therefore it’s possible for invalid data<br>        # to enter your database if you don’t manually call the full_clean<br>        # function before saving.<br><br>        # Object managers’ default create function also doesn’t call full_clean.<br><br>        # But in general, it's not good practice to add validation in the<br>        # save() method. The reason is that in most Django apps, you'd create<br>        # a form (a ModelForm) which would call the validation methods and be<br>        # able to return something meaningful to the user when validation<br>        # fails.<br><br>        # When the model's save() method is called it's too late to show<br>        # something to the user, so you can only raise an exception at that<br>        # point (and crash).<br><br>        # The normal procedure (which the admin forms use) is: validate the<br>        # form by calling form.is_valid() (which calls full_clean() on the<br>        # model), then if and only if the form is valid, save the model.<br><br>        # The shell is not the regular interaction method and should be used<br>        # only very carefully as it bypasses the normal flow of the<br>        # application.<br><br><br><br>    def create_user(self, email, password=None, **extra_fields):<br>        """Create and save a regular User with the given email and password."""<br>        <br>        extra_fields.setdefault('is_staff', False)<br>        extra_fields.setdefault('is_superuser', False)<br><br>        # What setdefault function does is that while creating a user if the<br>        # calling function  is not providing any values then set is_staff and<br>        # is_superuser both to False for this user.<br><br>        # we want to save the email as lower.<br>        return self._create_user(email.lower(), password, **extra_fields)<br><br>    def create_superuser(self, email, password, **extra_fields):<br>        """Create and save a SuperUser with the given email and password."""<br><br>        #For superuser to login to admin the following three conditions should<br>        #be satisfied<br><br>        # is_staff  =&gt; True  (if exit).<br>        # is_active  =&gt; True .<br>        # is_superuser =&gt; True.<br><br>        #Set the values if they are not defined<br><br>        extra_fields.setdefault('is_staff', True)<br>        extra_fields.setdefault('is_superuser', True)<br>        extra_fields.setdefault('is_active', True)<br><br>        #Option1: (Change the values internally irrespective of the user input)<br>        <br>        # We want for super user is_staff, is_superuser and is_active to be<br>        # true. So the below will change the value to True even if someone<br>        # passes False to any value. But this approach is not good since the<br>        # user will not know that his values are getting manupulated. <br>        <br><br>        # extra_fields['is_staff'] = True<br>        # extra_fields['is_superuser'] = True<br>        # extra_fields['is_active'] = True<br><br>        #Option2:<br>        <br>        # Check the values provided, if not True raise exception<br>        # The below approach is preferred so that the end user knows that he supplied wrong data.<br><br><br>        if extra_fields.get('is_staff') is not True:<br>            raise ValueError('Superuser must have is_staff=True.')<br>        if extra_fields.get('is_superuser') is not True:<br>            raise ValueError('Superuser must have is_superuser=True.')<br>        if extra_fields.get('is_active') is not True:<br>            raise ValueError('Superuser must have is_superuser=True.')<br><br>        # what is need for setdefault and again raise error<br><br>        # setdefault sets the value only if the key is not already present in the dict. <br>        # The caller of the function could still pass extra_fields with some values of id_staff <br>        # or is_superuser.<br><br>        # What this function does is that while creating a superuser if the calling function <br>        # is not providing any values then set is_staff and is_superuser both to True for this user.<br><br>        # But, if the values are provided then check if those are True and <br>        # raise exceptions otherwise.<br><br><br>        # we want to save the email as lower.<br>        return self._create_user(email.lower(), password, **extra_fields)<br><br><br># To have custom fields in the User we have to create a Model which inheret AbscratcUser<br># Reason: The auth model contain the User model. Which we cannot modify. So we have to inheret<br># AbstractUser class so that we can change it.<br><br># Below we are creating BaseUser Abstract Class from another Abstract class AbstractUser<br># Later Below this class we will inheret it in User class<br><br>class BaseUser(AbstractUser):<br>    """User model."""<br><br>    # We are inheriting AbstractUser and username is already defined there<br>    # We dont want to use username as we will be using email as login<br>    # inorder to not use username we say username = None<br>    username = None<br><br>    #we want to login via otp also without setting password. In that case we<br>    #want to create a random password<br>    #overrides password defined in AbstractBaseUser <br>    random_string = generateSecureRandomString()<br>    random_string_hassed = make_password(random_string)<br>    password=models.CharField(_('password'), max_length=128,default=random_string_hassed)<br><br>    # AbstractBaseUser has last_login. But here we are loging via 2 menthods so we need more variables<br>    recentdate_login_via_passwd = models.DateTimeField(_('last login via password'), blank=True, null=True)<br>    recentdate_login_via_otp = models.DateTimeField(_('last login via otp'), blank=True, null=True)<br>    recentdate_password_change = models.DateTimeField(_('last password change'), blank=True, null=True)<br><br>    # We are inheriting AbstractUser and first_name and last_name are already defined there<br>    # We want first_name and last name to be entered compulsory, But in the AbstactUser it<br>    # says blank=TRUE. So we have to rewrite it so redefine again without blank=True<br>    first_name = models.CharField(_('first name'), max_length=30,blank=True)<br>    # NULL allowed, but will never be set as NULL<br>    # The exception is CharFields and TextFields, which in Django are never saved as NULL. Blank values are stored in the DB as an empty string ('').<br>    last_name = models.CharField(_('last name'), max_length=150,blank=True)<br><br><br>    # We are inheriting AbstractUser and email is already defined there<br>    # its defined as blank=TRUE in the AbstractUser.<br>    # But we will be using it as the login field and also want to be unique<br>    email = models.EmailField(<br>        _('email address'),<br>        help_text="Please Enter valid Email Address",<br>        unique=True,<br>        error_messages={<br>            'unique': _("This email already exists."),<br>        },<br>    )<br><br>    # We are inheriting AbstractUser and is_active is already defined there<br>    # We dont want a user to be active unless his email is confirmed<br>    # we modify it with default=False<br>    is_active = models.BooleanField(<br>        _('active'),<br>        default=False,<br>        help_text=_(<br>            'Designates whether this user should be treated as active. '<br>            'Unselect this instead of deleting accounts.'<br>        )<br>    )<br><br>    # NULL allowed, but will never be set as NULL<br>    # The exception is CharFields and TextFields, which in Django are never saved as NULL. Blank values are stored in the DB as an empty string ('').<br>    recent_otp_used_for_pass_change = models.CharField(<br>        _('otp'),<br>        help_text="Please Enter valid OTP sent to your Email",<br>        max_length=6,<br>        validators=[<br>            RegexValidator(<br>                r'^\d{6}$',<br>                message=_('OTP shoud be of 6 digits'),<br>                code='invalid'<br>            )<br>        ]<br>    )<br><br>    date_of_recent_otp_used_for_pass_change = models.DateTimeField(null=True)<br><br>    # when we create a login and pass singup form, we try to verify the email then this is required<br>    otp_used_while_passlogin_create = models.CharField(<br>        _('otp'),<br>        help_text="Please Enter valid OTP sent to your Email",<br>        max_length=6,<br>        validators=[<br>            RegexValidator(<br>                r'^\d{6}$',<br>                message=_('OTP shoud be of 6 digits'),<br>                code='invalid'<br>            )<br>        ]<br>    )<br><br>    date_of_otp_used_while_passlogin_create = models.DateTimeField(null=True)<br><br>    first_otp_used_for_otplogin = models.CharField(<br>        _('otp'),<br>        help_text="Please Enter valid OTP sent to your Email",<br>        max_length=6,<br>        validators=[<br>            RegexValidator(<br>                r'^\d{6}$',<br>                message=_('OTP shoud be of 6 digits'),<br>                code='invalid'<br>            )<br>        ]<br>    )<br><br>    date_of_first_otp_used_for_otplogin = models.DateTimeField(null=True)<br><br><br>    # List of fields inhereted from AbstractUser<br>    # is_staff    #'Designates whether the user can log into this admin site.'<br>    # date_joined<br><br>    # List of fields inhereted from AbstractBaseUser<br>    # password<br>    # last_login<br>    # is_active<br><br><br>    # Optional fields to be filled by user for more information<br>    about = models.TextField(max_length=500, blank=True)<br>    location = models.CharField(max_length=30, blank=True)<br>    birth_date = models.DateField(null=True, blank=True)<br>    <br><br>    modified_date = models.DateTimeField(_('modified date'),auto_now=True)<br><br>    creation_date = models.DateTimeField(_('creation date'),auto_now_add=True)<br><br>    # Because last_login is set by the signal in login() we dont want it and instead have our own<br>    last_login2 = models.DateTimeField(_('last login 2'), blank=True, null=True)<br><br>    # A string describing the name of the field on the user model that is <br>    # used as the unique identifier. This will usually be a username of <br>    # some kind, but it can also be an email address, or any other unique <br>    # identifier. The field must be unique (i.e., have unique=True set in its <br>    # definition), unless you use a custom authentication backend that can <br>    # support non-unique usernames.<br>    USERNAME_FIELD = 'email'<br><br>    # REQUIRED_FIELDS DEFINITION<br>    # A list of the field names that will be prompted for when creating a user <br>    # via the createsuperuser management command. The user will be prompted to <br>    # supply a value for each of these fields. It must include any field for which <br>    # blank is False or undefined and may include additional fields you want prompted <br>    # for when a user is created interactively. REQUIRED_FIELDS has no effect in other <br>    # parts of Django, like creating a user in the admin.<br><br>    # presently we dont want to be asked for anything while createsuperuser<br>    REQUIRED_FIELDS = []<br><br>    class Meta:<br>        """Define Meta class for BaseUser model."""<br>        # We want this class to be abstract so we define the below<br>        abstract = True <br><br>    # def jwt_get_secret_key(self):<br>    #     return self.jwt_secret<br><br><br><br># Finally Inheret BaseUser class (Why we are using this way is to have flexibility later)<br># This how the actual /venv_btg/lib/python3.6/site-packages/django/contrib/auth/models.py is done<br># Ofcouse there is no need to do this but we just keep it like the /auth/models.py say<br><br>class User(BaseUser):<br>    objects = UserManager()<br><br>    # the below Meta class is added in /venv_btg/lib/python3.6/site-packages/django/contrib/auth/models.py<br>    # User model<br><br>    class Meta(BaseUser.Meta):<br>        swappable = 'AUTH_USER_MODEL'<br><br><br><br><br>from django.contrib.auth import get_user_model<br><br>def get_sentinel_user():<br>    try:<br>        match = get_user_model().objects.get(email='deleted')<br>    except:<br>        match = get_user_model().objects.create(email='deleted',last_login2=timezone.now())<br>    return match<br><br>class ActionTypeForUserSessionLog(models.Model):<br>    action = models.CharField(max_length=100, blank=False,unique=True)<br><br>class UserSessionLog(models.Model):<br>    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET(get_sentinel_user))<br>    user_email =    models.EmailField()<br>    otp_used_for_pass_change = models.CharField(<br>        _('otp'),<br>        help_text="Please Enter valid OTP sent to your Email",<br>        max_length=6,<br>        validators=[<br>            RegexValidator(<br>                r'^\d{6}$',<br>                message=_('OTP shoud be of 6 digits'),<br>                code='invalid'<br>            )<br>        ]<br>    )<br><br>    otp_used_while_passlogin_create = models.CharField(<br>        _('otp'),<br>        help_text="Please Enter valid OTP sent to your Email",<br>        max_length=6,<br>        validators=[<br>            RegexValidator(<br>                r'^\d{6}$',<br>                message=_('OTP shoud be of 6 digits'),<br>                code='invalid'<br>            )<br>        ]<br>    )<br><br>    otp_used_for_otplogin = models.CharField(<br>        _('otp'),<br>        help_text="Please Enter valid OTP sent to your Email",<br>        max_length=6,<br>        validators=[<br>            RegexValidator(<br>                r'^\d{6}$',<br>                message=_('OTP shoud be of 6 digits'),<br>                code='invalid'<br>            )<br>        ]<br>    )<br><br>    device_type = models.CharField(max_length=255)<br>    ip_address = models.GenericIPAddressField()<br>    created_time = models.DateTimeField(default=timezone.now)<br>    action_type = models.ForeignKey(ActionTypeForUserSessionLog, on_delete=models.PROTECT)<br><br><br><br><br><br>#We have to pass initial data to ActionTypeForUserSessionLog model:<br>#https://docs.djangoproject.com/en/2.2/howto/initial-data/#providing-data-with-fixtures<br>#Create a fixtures folder in any app and then name it something then do<br># manage.py loaddata something.<br><br>#You’ll store this data in a fixtures directory inside your app.<br><br>#Loading data is easy: just call manage.py loaddata &lt;fixturename&gt;, where<br>#&lt;fixturename&gt; is the name of the fixture file you’ve created. Each time you run<br>#loaddata, the data will be read from the fixture and re-loaded into the<br>#database. Note this means that if you change one of the rows created by a<br>#fixture and then run loaddata again, you’ll wipe out any changes you’ve made.<br><br><br><br>###    [<br>###      {<br>###        "model": "custom_user.ActionTypeForUserSessionLog",<br>###        "pk": 1,<br>###        "fields": {<br>###          "action": "pass_change",<br>###        }<br>###      },<br>###      {<br>###        "model": "custom_user.ActionTypeForUserSessionLog",<br>###        "pk": 2,<br>###        "fields": {<br>###          "action": "login_by_otp",<br>###        }<br>###      },<br>###      {<br>###        "model": "custom_user.ActionTypeForUserSessionLog",<br>###        "pk": 3,<br>###        "fields": {<br>###          "action": "login_by_pass",<br>###        }<br>###      },<br>###      {<br>###        "model": "custom_user.ActionTypeForUserSessionLog",<br>###        "pk": 4,<br>###        "fields": {<br>###          "action": "passlogin_email_validation",<br>###        }<br>###      }<br>###    ]<br></td></tr></tbody></table>

 * ## \[image\] models.py (full code)

     * ![](images/image166.png)![](images/image33.png)![](images/image42.png)![](images/image7.png)![](images/image213.png)![](images/image86.png)![](images/image9.png)![](images/image65.png)![](images/image79.png)![](images/image199.png)![](images/image179.png)![](images/image97.png)

 * ## \[code\] Integrate custom\_user with admin module

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>""" Integrate custom_user with admin module. """<br><br>from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin<br>from django.utils.translation import ugettext_lazy as _<br><br>from django.contrib import admin<br>from .models import User<br><br><br>class BaseUserAdmin(DjangoUserAdmin):<br>    """Define admin model for custom User model with no email field."""<br><br>    fieldsets = (<br>        (None, {<br>            'fields': ('email', 'password')<br>        }),<br>        (_('Personal info'), {<br>            'fields': ('first_name', 'last_name')<br>        }),<br>        (_('Permissions'), {<br>            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')<br>        }),<br>        (_('Important dates'), {<br>            'fields': ('last_login', 'date_joined')<br>        }),<br>    )<br>    add_fieldsets = ((None, {<br>        'classes': ('wide', ),<br>        'fields': ('email', 'password1', 'password2'),<br>    }), )<br>    list_display = ('email', 'first_name', 'last_name', 'is_staff')<br>    search_fields = ('email', 'first_name', 'last_name')<br>    ordering = ('email', )<br><br><br>admin.site.register(User, BaseUserAdmin)<br></td></tr></tbody></table>

 * ## \[image\] admin.py

     * ![](images/image21.png)![](images/image180.png)

 * ## \[code\]Change in Settings

     * Add the following in settings.py

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>#gauranga<br>AUTH_USER_MODEL = 'custom_user.User<br></td></tr></tbody></table>

 * ## \[image\] settings.py

     * ![](images/image211.png)

 * ## 1.RUNNING MIGRATION FOR FIRST TIME

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>    $ python manage.py makemigrations<br>    $ python manage.py migrate<br><br><br>$ python manage.py makemigrations<br><br>Migrations for 'custom_user':<br>  custom_user/migrations/0001_initial.py<br>    - Create model User<br><br> simha  ...web_dev/django_basic_documentation/basic_django  🐍 django_basic_documentation-4mWf8-Zv   master ✘ ✚ ✭<br>$ python manage.py migrate       <br><br>Operations to perform:<br>  Apply all migrations: admin, auth, contenttypes, custom_user, sessions<br>Running migrations:<br>  Applying contenttypes.0001_initial... OK<br>  Applying contenttypes.0002_remove_content_type_name... OK<br>  Applying auth.0001_initial... OK<br>  Applying auth.0002_alter_permission_name_max_length... OK<br>  Applying auth.0003_alter_user_email_max_length... OK<br>  Applying auth.0004_alter_user_username_opts... OK<br>  Applying auth.0005_alter_user_last_login_null... OK<br>  Applying auth.0006_require_contenttypes_0002... OK<br>  Applying auth.0007_alter_validators_add_error_messages... OK<br>  Applying auth.0008_alter_user_username_max_length... OK<br>  Applying auth.0009_alter_user_last_name_max_length... OK<br>  Applying auth.0010_alter_group_name_max_length... OK<br>  Applying auth.0011_update_proxy_permissions... OK<br>  Applying custom_user.0001_initial... OK<br>  Applying admin.0001_initial... OK<br>  Applying admin.0002_logentry_remove_auto_add... OK<br>  Applying admin.0003_logentry_add_action_flag_choices... OK<br>  Applying sessions.0001_initial... OK<br><br><br></td></tr></tbody></table>

 * ## \[code\] migrate with sql commands executed

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>$ python manage.py migrate      Operations to perform:<br>  Apply all migrations: admin, auth, contenttypes, custom_user, sessions<br>Running migrations:<br>CREATE TABLE "django_migrations" ("id" serial NOT NULL PRIMARY KEY, "app" varchar(255) NOT NULL, "name" varchar(255) NOT NULL, "applied" timestamp with time zone NOT NULL); (params None)<br><br>CREATE TABLE "django_content_type" ("id" serial NOT NULL PRIMARY KEY, "name" varchar(100) NOT NULL, "app_label" varchar(100) NOT NULL, "model" varchar(100) NOT NULL); (params None)<br><br>ALTER TABLE "django_content_type" ADD CONSTRAINT "django_content_type_app_label_model_76bd3d3b_uniq" UNIQUE ("app_label", "model"); (params ())<br><br>  Applying contenttypes.0001_initial... OK<br><br>ALTER TABLE "django_content_type" ALTER COLUMN "name" DROP NOT NULL; (params [])<br><br>ALTER TABLE "django_content_type" DROP COLUMN "name" CASCADE; (params ())<br><br>  Applying contenttypes.0002_remove_content_type_name... OK<br><br>CREATE TABLE "auth_permission" ("id" serial NOT NULL PRIMARY KEY, "name" varchar(50) NOT NULL, "content_type_id" integer NOT NULL, "codename" varchar(100) NOT NULL); (params None)<br><br>CREATE TABLE "auth_group" ("id" serial NOT NULL PRIMARY KEY, "name" varchar(80) NOT NULL UNIQUE); (params None)<br><br>CREATE TABLE "auth_group_permissions" ("id" serial NOT NULL PRIMARY KEY, "group_id" integer NOT NULL, "permission_id" integer NOT NULL); (params None)<br><br>ALTER TABLE "auth_permission" ADD CONSTRAINT "auth_permission_content_type_id_2f476e4b_fk_django_co" FOREIGN KEY ("content_type_id") REFERENCES "django_content_type" ("id") DEFERRABLE INITIALLY DEFERRED; (params ())<br><br>ALTER TABLE "auth_permission" ADD CONSTRAINT "auth_permission_content_type_id_codename_01ab375a_uniq" UNIQUE ("content_type_id", "codename"); (params ())<br><br>CREATE INDEX "auth_permission_content_type_id_2f476e4b" ON "auth_permission" ("content_type_id"); (params ())<br><br>CREATE INDEX "auth_group_name_a6ea08ec_like" ON "auth_group" ("name" varchar_pattern_ops); (params ())<br><br>ALTER TABLE "auth_group_permissions" ADD CONSTRAINT "auth_group_permissions_group_id_b120cbf9_fk_auth_group_id" FOREIGN KEY ("group_id") REFERENCES "auth_group" ("id") DEFERRABLE INITIALLY DEFERRED; (params ())<br><br>ALTER TABLE "auth_group_permissions" ADD CONSTRAINT "auth_group_permissio_permission_id_84c5c92e_fk_auth_perm" FOREIGN KEY ("permission_id") REFERENCES "auth_permission" ("id") DEFERRABLE INITIALLY DEFERRED; (params ())<br><br>ALTER TABLE "auth_group_permissions" ADD CONSTRAINT "auth_group_permissions_group_id_permission_id_0cd325b0_uniq" UNIQUE ("group_id", "permission_id"); (params ())<br><br>CREATE INDEX "auth_group_permissions_group_id_b120cbf9" ON "auth_group_permissions" ("group_id"); (params ())<br><br>CREATE INDEX "auth_group_permissions_permission_id_84c5c92e" ON "auth_group_permissions" ("permission_id"); (params ())<br><br>  Applying auth.0001_initial... OK<br><br>ALTER TABLE "auth_permission" ALTER COLUMN "name" TYPE varchar(255) USING "name"::varchar(255); (params [])<br><br>  Applying auth.0002_alter_permission_name_max_length... OK<br>  Applying auth.0003_alter_user_email_max_length... OK<br>  Applying auth.0004_alter_user_username_opts... OK<br>  Applying auth.0005_alter_user_last_login_null... OK<br>  Applying auth.0006_require_contenttypes_0002... OK<br>  Applying auth.0007_alter_validators_add_error_messages... OK<br>  Applying auth.0008_alter_user_username_max_length... OK<br>  Applying auth.0009_alter_user_last_name_max_length... OK<br><br>ALTER TABLE "auth_group" ALTER COLUMN "name" TYPE varchar(150) USING "name"::varchar(150); (params [])<br><br>  Applying auth.0010_alter_group_name_max_length... OK<br>  Applying auth.0011_update_proxy_permissions... OK<br><br>CREATE TABLE "custom_user_user" ("id" serial NOT NULL PRIMARY KEY, "last_login" timestamp with time zone NULL, "is_superuser" boolean NOT NULL, "is_staff" boolean NOT NULL, "date_joined" timestamp with time zone NOT NULL, "password" varchar(128) NOT NULL, "recentdate_login_via_passwd" timestamp with time zone NULL, "recentdate_login_via_otp" timestamp with time zone NULL, "recentdate_password_change" timestamp with time zone NULL, "first_name" varchar(30) NOT NULL, "last_name" varchar(150) NOT NULL, "email" varchar(254) NOT NULL UNIQUE, "is_active" boolean NOT NULL, "recent_otp_used_for_pass_change" varchar(6) NOT NULL, "date_of_recent_otp_used_for_pass_change" timestamp with time zone NULL, "otp_used_while_passlogin_create" varchar(6) NOT NULL, "date_of_otp_used_while_passlogin_create" timestamp with time zone NULL, "first_otp_used_for_otplogin" varchar(6) NOT NULL, "date_of_first_otp_used_for_otplogin" timestamp with time zone NULL, "about" text NOT NULL, "location" varchar(30) NOT NULL, "birth_date" date NULL, "modified_date" timestamp with time zone NOT NULL, "creation_date" timestamp with time zone NOT NULL, "last_login2" timestamp with time zone NOT NULL); (params None)<br><br>CREATE TABLE "custom_user_user_groups" ("id" serial NOT NULL PRIMARY KEY, "user_id" integer NOT NULL, "group_id" integer NOT NULL); (params None)<br><br>CREATE TABLE "custom_user_user_user_permissions" ("id" serial NOT NULL PRIMARY KEY, "user_id" integer NOT NULL, "permission_id" integer NOT NULL); (params None)<br><br>CREATE TABLE "custom_user_actiontypeforusersessionlog" ("id" serial NOT NULL PRIMARY KEY, "action" varchar(100) NOT NULL UNIQUE); (params None)<br><br>CREATE TABLE "custom_user_usersessionlog" ("id" serial NOT NULL PRIMARY KEY, "user_email" varchar(254) NOT NULL, "otp_used_for_pass_change" varchar(6) NOT NULL, "otp_used_while_passlogin_create" varchar(6) NOT NULL, "otp_used_for_otplogin" varchar(6) NOT NULL, "device_type" varchar(255) NOT NULL, "ip_address" inet NOT NULL, "created_time" timestamp with time zone NOT NULL, "action_type_id" integer NOT NULL, "user_id" integer NOT NULL); (params None)<br><br>CREATE INDEX "custom_user_user_email_a19d9305_like" ON "custom_user_user" ("email" varchar_pattern_ops); (params ())<br><br>ALTER TABLE "custom_user_user_groups" ADD CONSTRAINT "custom_user_user_groups_user_id_f1071bc9_fk_custom_user_user_id" FOREIGN KEY ("user_id") REFERENCES "custom_user_user" ("id") DEFERRABLE INITIALLY DEFERRED; (params ())<br><br>ALTER TABLE "custom_user_user_groups" ADD CONSTRAINT "custom_user_user_groups_group_id_dfde52bf_fk_auth_group_id" FOREIGN KEY ("group_id") REFERENCES "auth_group" ("id") DEFERRABLE INITIALLY DEFERRED; (params ())<br><br>ALTER TABLE "custom_user_user_groups" ADD CONSTRAINT "custom_user_user_groups_user_id_group_id_fc2104d2_uniq" UNIQUE ("user_id", "group_id"); (params ())<br><br>CREATE INDEX "custom_user_user_groups_user_id_f1071bc9" ON "custom_user_user_groups" ("user_id"); (params ())<br><br>CREATE INDEX "custom_user_user_groups_group_id_dfde52bf" ON "custom_user_user_groups" ("group_id"); (params ())<br><br>ALTER TABLE "custom_user_user_user_permissions" ADD CONSTRAINT "custom_user_user_use_user_id_65556ab9_fk_custom_us" FOREIGN KEY ("user_id") REFERENCES "custom_user_user" ("id") DEFERRABLE INITIALLY DEFERRED; (params ())<br><br>ALTER TABLE "custom_user_user_user_permissions" ADD CONSTRAINT "custom_user_user_use_permission_id_cb2d2b0f_fk_auth_perm" FOREIGN KEY ("permission_id") REFERENCES "auth_permission" ("id") DEFERRABLE INITIALLY DEFERRED; (params ())<br><br>ALTER TABLE "custom_user_user_user_permissions" ADD CONSTRAINT "custom_user_user_user_pe_user_id_permission_id_2215a086_uniq" UNIQUE ("user_id", "permission_id"); (params ())<br><br>CREATE INDEX "custom_user_user_user_permissions_user_id_65556ab9" ON "custom_user_user_user_permissions" ("user_id"); (params ())<br><br>CREATE INDEX "custom_user_user_user_permissions_permission_id_cb2d2b0f" ON "custom_user_user_user_permissions" ("permission_id"); (params ())<br><br>CREATE INDEX "custom_user_actiontypeforusersessionlog_action_60e49b6c_like" ON "custom_user_actiontypeforusersessionlog" ("action" varchar_pattern_ops); (params ())<br><br>ALTER TABLE "custom_user_usersessionlog" ADD CONSTRAINT "custom_user_usersess_action_type_id_c1903e6a_fk_custom_us" FOREIGN KEY ("action_type_id") REFERENCES "custom_user_actiontypeforusersessionlog" ("id") DEFERRABLE INITIALLY DEFERRED; (params ())<br><br>ALTER TABLE "custom_user_usersessionlog" ADD CONSTRAINT "custom_user_usersess_user_id_13ffa01e_fk_custom_us" FOREIGN KEY ("user_id") REFERENCES "custom_user_user" ("id") DEFERRABLE INITIALLY DEFERRED; (params ())<br><br>CREATE INDEX "custom_user_usersessionlog_action_type_id_c1903e6a" ON "custom_user_usersessionlog" ("action_type_id"); (params ())<br><br>CREATE INDEX "custom_user_usersessionlog_user_id_13ffa01e" ON "custom_user_usersessionlog" ("user_id"); (params ())<br><br>  Applying custom_user.0001_initial... OK<br><br>CREATE TABLE "django_admin_log" ("id" serial NOT NULL PRIMARY KEY, "action_time" timestamp with time zone NOT NULL, "object_id" text NULL, "object_repr" varchar(200) NOT NULL, "action_flag" smallint NOT NULL CHECK ("action_flag" &gt;= 0), "change_message" text NOT NULL, "content_type_id" integer NULL, "user_id" integer NOT NULL); (params None)<br><br>ALTER TABLE "django_admin_log" ADD CONSTRAINT "django_admin_log_content_type_id_c4bce8eb_fk_django_co" FOREIGN KEY ("content_type_id") REFERENCES "django_content_type" ("id") DEFERRABLE INITIALLY DEFERRED; (params ())<br><br>ALTER TABLE "django_admin_log" ADD CONSTRAINT "django_admin_log_user_id_c564eba6_fk_custom_user_user_id" FOREIGN KEY ("user_id") REFERENCES "custom_user_user" ("id") DEFERRABLE INITIALLY DEFERRED; (params ())<br><br>CREATE INDEX "django_admin_log_content_type_id_c4bce8eb" ON "django_admin_log" ("content_type_id"); (params ())<br><br>CREATE INDEX "django_admin_log_user_id_c564eba6" ON "django_admin_log" ("user_id"); (params ())<br><br>  Applying admin.0001_initial... OK<br>  Applying admin.0002_logentry_remove_auto_add... OK<br>  Applying admin.0003_logentry_add_action_flag_choices... OK<br>  <br>CREATE TABLE "django_session" ("session_key" varchar(40) NOT NULL PRIMARY KEY, "session_data" text NOT NULL, "expire_date" timestamp with time zone NOT NULL); (params None)<br><br>CREATE INDEX "django_session_session_key_c0390e0f_like" ON "django_session" ("session_key" varchar_pattern_ops); (params ())<br><br>CREATE INDEX "django_session_expire_date_a5c62663" ON "django_session" ("expire_date"); (params ())<br><br>  Applying sessions.0001_initial... OK<br><br><br></td></tr></tbody></table>

 * ## \[image\] makemigrationa and migrate

     * ![](images/image202.png)

 * ## \[image\] migrate output with sql

     * ![](images/image218.png)![](images/image96.png)![](images/image94.png)![](images/image137.png)![](images/image40.png)

 * ## \[image\]                         Look at the table created after migration in postgresql:

     * ![](images/image205.png)

 * ## Initialize the ActionTypeForUserSessionLog Table

     * To initialize data we use fixtures

     * For that we create a folder fixtures and create a file ActionTypeForUserSessionLog.json in it

     * ### \[code\] ActionTypeForUserSessionLog.json

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>[{<br>    "model": "custom_user.ActionTypeForUserSessionLog",<br>    "pk": 1,<br>    "fields": {<br>      "action": "pass_change"<br>    }<br>  },<br>  {<br>    "model": "custom_user.ActionTypeForUserSessionLog",<br>    "pk": 2,<br>    "fields": {<br>      "action": "login_by_otp"<br>    }<br>  },<br>  {<br>    "model": "custom_user.ActionTypeForUserSessionLog",<br>    "pk": 3,<br>    "fields": {<br>      "action": "login_by_pass"<br>    }<br>  },<br>  {<br>    "model": "custom_user.ActionTypeForUserSessionLog",<br>    "pk": 4,<br>    "fields": {<br>      "action": "passlogin_email_validation"<br>    }<br>  }<br>]<br><br></td></tr></tbody></table>

       * Then run the following command to insert the data

     * ### \[code\] insert

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>#gauranga<br>$ python manage.py loaddata custom_user/fixtures/ActionTypeForUserSessionLog.json<br></td></tr></tbody></table>

* # NINTH COMMIT END

* # TENTH COMMIT START

 * ## Philosophy behind admin page

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>Philosophy<br>Generating admin sites for your staff or clients to add, change and delete content is tedious work that doesn’t require much creativity. For that reason, Django entirely automates creation of admin interfaces for models.<br>Django was written in a newsroom environment, with a very clear separation between “content publishers” and the “public” site. Site managers use the system to add news stories, events, sports scores, etc., and that content is displayed on the public site. Django solves the problem of creating a unified interface for site administrators to edit content.<br>The admin isn’t intended to be used by site visitors. It’s for site managers.<br><br>By default the admin urls are added to the urls.py<br>/basic_django/basic_django/urls.py<br><br>from django.contrib import admin<br>from django.urls import path<br><br>urlpatterns = [<br>    path('admin/', admin.site.urls),<br>]<br><br></td></tr></tbody></table>

 * ## Creating an admin user¶

     * First we’ll need to create a user who can login to the admin site. Run the following command:

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>#gauranga<br>$ python manage.py createsuperuser<br>Email address: xyz@asb.com<br>Password: <br>Password (again): <br>Superuser created successfully.<br></td></tr></tbody></table>

 * ## Start the development server

     * The Django admin site is activated by default. Let’s start the development server and explore it.

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>#gauranga<br>$ python manage.py runserver<br></td></tr></tbody></table>

     * Now, open a Web browser and go to “/admin/” on your local domain – e.g., http://127.0.0.1:8000/admin/. You should see the admin’s login screen:

     * ![](images/image76.png)

 * ## How to reset Django admin password?

     * Somtimes we may have forgot the admin password so we can change the password

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>#gauranga<br>$ python manage.py changepassword &lt;user_name&gt;<br>Changing password for user ' xyz@asb.com'<br>Password: <br>Password (again): <br>Password changed successfully for user ' xyz@asb.com'<br></td></tr></tbody></table>

 * ## If admin login does not work

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>Check in the custom_user_user table <br><br>Is_active = TRUE<br>Is_superuser = TRUE<br>Is_staff = TRUE<br><br>If any them is  false then check the function for create_superuser<br><br>    def create_superuser(self, email, password, **extra_fields):<br>        """Create and save a SuperUser with the given email and password."""<br><br>        #For superuser to login to admin the following three conditions should<br>        #be satisfied<br><br>        # is_staff  =&gt; True  (if exit).<br>        # is_active  =&gt; True .<br>        # is_superuser =&gt; True.<br><br>        #Set the values if they are not defined<br><br>        # is_staff  =&gt; True  (if exit).<br>        # is_active  =&gt; True .<br>        # is_superuser =&gt; True.<br><br>        extra_fields.setdefault('is_staff', True)<br>        extra_fields.setdefault('is_superuser', True)<br>        extra_fields.setdefault('is_active', True)<br>        if extra_fields.get('is_staff') is not True:<br>            raise ValueError('Superuser must have is_staff=True.')<br>        if extra_fields.get('is_superuser') is not True:<br>            raise ValueError('Superuser must have is_superuser=True.')<br>        if extra_fields.get('is_active') is not True:<br>            raise ValueError('Superuser must have is_superuser=True.')<br><br>        # what is need for setdefault and again raise error<br><br>        # setdefault sets the value only if the key is not already present in the dict. <br>        # The caller of the function could still pass extra_fields with some values of id_staff <br>        # or is_superuser.<br><br>        # What this function does is that while creating a superuser if the calling function <br>        # is not providing any values then set is_staff and is_superuser both to True for this user.<br><br>        # But, if the values are provided then check if those are True and <br>        # raise exceptions otherwise.<br><br><br>        # we want to save the email as lower.<br>        return self._create_user(email.lower(), password, **extra_fields)<br> <br></td></tr></tbody></table>

* # TENTH COMMIT END

* # ELEVENTH COMMIT START

 * ## Create an app called login\_register\_password and articles  

     * Note: we cant use name ‘login’ alone because “it conflicts with the name of an existing Python module and cannot be used as an app name. Please try another name.”

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>#gauranga<br>python manage.py startapp  login_register_password   #means logging via otp/password, register for password login and password reset<br><br>python manage.py startapp articles # this if for home page.<br></td></tr></tbody></table>

     * ### \[image\] Directory tree (sorted w.r.t time desc) after startapp

       * ![](images/image227.png)

* # ELEVENTH COMMIT END

* # ELEVENTH\_A COMMIT START

     * And add to the settings.py

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td># Application definition<br><br>INSTALLED_APPS = [<br>    'django.contrib.admin',<br>    'django.contrib.auth',<br>    'django.contrib.contenttypes',<br>    'django.contrib.sessions',<br>    'django.contrib.messages',<br>    'django.contrib.staticfiles',<br>    'custom_user',<br>    'login_register_password',<br>    'articles'<br>]<br></td></tr></tbody></table>

     * ### \[image\]

       * ![](images/image91.png)

* # ELEVENTH\_A COMMIT END

* # TWELVETH COMMIT START

 * ## Aim: To create a login via email and OTP. 

     * The below images will shows the urls and the flow

     * ### \[image\] Home Page

       * ![](images/image72.png)

       * Now one wants to login (may be to comment etc) will click on login

     * ### \[image\] Email form

       * ![](images/image103.png)

     * ### \[image\] OTP form

       * ![](images/image44.png)

     * ### \[image\] Login confirmation and back to home page

       * ![](images/image102.png)

       * One wants to logout, He will click logout

     * ### \[image\] Logout confirmation and back to home page

       * ![](images/image147.png)

 * ## Install pyjwt

     * Pyjwt is used to create jwt tokens.

     * ### \[code\]

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>#gauranga<br>Pipenv install pyjwt<br><br>Usage:<br>Create a jwt token:<br><br>from django.utils import timezone<br>import datetime<br>import pytz<br>payload = {<br>    'email': email,<br>    'OTP': pin,<br>    'creation_time': str(datetime.datetime.now(tz=pytz.timezone('UTC')).isoformat())<br>}<br>jwt_token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256').decode('utf-8')<br><br><br>decode a jwt token:<br><br>payload = jwt.decode(<br>    jwt_token,<br>    settings.SECRET_KEY,<br>    True,<br>)<br><br></td></tr></tbody></table>

     * ### \[image\]

       * ![](images/image158.png)

 * ## Templates and Static files structure:

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>Template name space:<br><br>- some_app<br>    - templates<br>        - some_app<br>            - index.html<br><br>return render(request, some_app/index.html', Eg context {'title': title, 'cal': cal})<br><br>Static files name space<br><br>- some_app<br>    - static<br>        - some_app<br>            - css<br>                 - style.css<br>            - img<br>            - js<br><br> when you run collectstatic, each individual app's static files get placed inside a namespaced directory<br><br>{% load static %}<br>&lt;link rel="stylesheet" type="text/css" href="{% static some_app/css/style.css' %}"&gt;<br></td></tr></tbody></table>

     * Create template and static folders for articles and login\_register\_password

     * ### \[image\] template and static folders for login\_register\_password and articles

       * ![](images/image127.png)

 * ## MESSAGES For Templates:

     * We use messages to inform the user. It will save from modifying the template of the next page. 

     * /home/web\_dev/django\_basic\_documentation/basic\_django/basic\_django/settings.py

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>#By default, Django will only display messages with level greater than 20<br>#(INFO). If you want to display DEBUG messages:<br>MESSAGE_LEVEL = 10  # DEBUG<br></td></tr></tbody></table>

     * ### \[image\]

       * ![](images/image170.png)

     * ### Using: And then in views.py call

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>from django.contrib import messages<br>messages.success(request, 'Email is being sent in TRY')<br></td></tr></tbody></table>

     * ### Clearing all messages

       * https://stackoverflow.com/a/51968838/2897115

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>        ## CLEARING ALL THE MESSAGES<br>        system_messages = messages.get_messages(request)<br>        for message in system_messages:<br>            # This iteration is necessary<br>            pass<br>        system_messages.used = Tru<br></td></tr></tbody></table>

 * ## TEMPLATES FOR login\_register\_password

     * ### base.html

       * /home/web\_dev/django\_basic\_documentation/basic\_django/login\_register\_password/templates/login\_register\_password/base.html

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>&lt;!DOCTYPE html&gt;<br>&lt;html&gt;<br>&lt;head&gt;<br>  &lt;meta charset="utf-8"&gt;<br>  &lt;title&gt;{% block title %}Django Auth Tutorial{% endblock %}&lt;/title&gt;<br>&lt;/head&gt;<br>&lt;body&gt;<br>        {% if messages %}<br>          &lt;ul class="messages"&gt;<br>            {% for message in messages %}<br>              &lt;li class="{{ message.tags }}"&gt;{{ message }}&lt;/li&gt;<br>            {% endfor %}<br>          &lt;/ul&gt;<br>        {% endif %}<br>  &lt;main&gt;<br>    {% block content %}<br>    {% endblock %}<br>  &lt;/main&gt;<br>&lt;/body&gt;<br>&lt;/html&gt;<br><br></td></tr></tbody></table>

     * ### \[image\]

       * ![](images/image226.png)

     * ### login\_via\_otp/user\_login\_via\_otp\_form\_email.html

       * /home/web\_dev/django\_basic\_documentation/basic\_django/login\_register\_password/templates/login\_register\_password/login\_via\_otp/user\_login\_via\_otp\_form\_email.html

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>{% extends 'login_register_password/base.html' %}<br><br>{% block title %}Login via OTP{% endblock %}<br><br>{% block content %}<br>  &lt;h2&gt;Login via OTP&lt;/h2&gt;<br>  &lt;form method="post"&gt;<br>    {% csrf_token %}<br>    {{ form.as_p }}<br>    &lt;button type="submit"&gt;Send OTP&lt;/button&gt;<br>  &lt;/form&gt;<br>{% endblock %}<br></td></tr></tbody></table>

     * ### \[image\]

       * ![](images/image177.png)

     * ### login\_via\_otp/user\_login\_via\_otp\_form\_otp.html

       * /home/web\_dev/django\_basic\_documentation/basic\_django/login\_register\_password/templates/login\_register\_password/login\_via\_otp/user\_login\_via\_otp\_form\_otp.html

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>{% extends 'login_register_password/base.html' %}<br><br>{% block title %}Enter otp{% endblock %}<br><br>{% block content %}<br>  &lt;h4&gt;Enter Otp&lt;/h4&gt;<br>  &lt;form method="post"&gt;<br>    {% csrf_token %}<br>    {{ form.as_p }}<br>    &lt;button type="submit"&gt;Login&lt;/button&gt;<br>  &lt;/form&gt;<br>  &lt;p&gt;If you dont recieve the otp click to resend again&lt;/p&gt;<br><br>&lt;form method="get"&gt;<br>        &lt;button type="submit" name="resendotp"&gt;Resend OTP&lt;/button&gt;<br>&lt;/form&gt;<br><br>{% endblock %}<br></td></tr></tbody></table>

     * ### \[image\]

       * ![](images/image116.png)

     * ### login\_via\_otp/email/login\_otp\_sendemail.html

       * /home/web\_dev/django\_basic\_documentation/basic\_django/login\_register\_password/templates/login\_register\_password/login\_via\_otp/email/login\_otp\_sendemail.html

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>{% autoescape off %}<br>Hi {{ user.email }},<br><br>Please enter the pin given below to login<br><br>{{ pin }}<br>{% endautoescape %}<br></td></tr></tbody></table>

     * ### \[image\]

       * ![](images/image83.png)

 * ## TEMPLATES FOR articles

     * ### base.html

       * /home/web\_dev/django\_basic\_documentation/basic\_django/articles/templates/articles/base.html

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>&lt;!DOCTYPE html&gt;<br>&lt;html&gt;<br>&lt;head&gt;<br>  &lt;meta charset="utf-8"&gt;<br>  &lt;title&gt;{% block title %}{% endblock %}&lt;/title&gt;<br>&lt;/head&gt;<br>&lt;body&gt;<br>        {% if messages %}<br>          &lt;ul class="messages"&gt;<br>            {% for message in messages %}<br>              &lt;li class="{{ message.tags }}"&gt;{{ message }}&lt;/li&gt;<br>            {% endfor %}<br>          &lt;/ul&gt;<br>        {% endif %}<br><br>        {% if user.is_authenticated %}<br>          Hi {{ user.email }}!<br>          &lt;p&gt;&lt;a href="{% url 'login_register_password_namespace:logout_view' %}"&gt;logout&lt;/a&gt;&lt;/p&gt;<br>        {% else %}<br>          &lt;p&gt;You are not logged in&lt;/p&gt;<br>          &lt;a href="{% url 'login_register_password_namespace:user_login_via_otp_form_email' %}"&gt;login&lt;/a&gt; |<br>          {% endif %}<br><br>  &lt;main&gt;<br>    {% block content %}<br>    {% endblock %}<br>  &lt;/main&gt;<br>&lt;/body&gt;<br>&lt;/html&gt;<br></td></tr></tbody></table>

     * ### \[image\]

       * ![](images/image32.png)

     * ### main\_page/articles.html

       * /home/web\_dev/django\_basic\_documentation/basic\_django/articles/templates/articles/main\_page/articles.html

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>{% extends 'articles/base.html' %}<br><br>{% block title %}Welcome to articles{% endblock %}<br><br>{% block content %}<br>  &lt;h2&gt;1) Sample article&lt;/h2&gt;<br>{% endblock %}<br></td></tr></tbody></table>

     * ### \[image\]

       * ![](images/image64.png)

 * ## Urls

     * Urls.py has to be created its not created by default. So create urls.py in articles and login\_register\_password. Also note the urls defined in each app (articles and login\_register\_password)  are included in the basic\_django/urls.py

     * The views names will be defined later in the Views section.

     * Url Name Spacing is very important

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>Urls.py of someapp_name<br>For every url we have (without include) : name<br>path('',views.articles, name='articles'),<br></td></tr></tbody></table>

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>Urls.py of someapp_name<br>For every app we have: app_name<br>app_name='articles_app_name'<br></td></tr></tbody></table>

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>Urls.py of base app<br>For include we have: namespace<br>path('someapp_name/', include('someapp_name.urls',namespace='someapp_name_namespace')),<br></td></tr></tbody></table>

     * If we defined namespace then app\_name is not needed

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>We call the urls in template as below using namespace<br>&lt;a href="{% url 'someapp_name_namespace:articles' %}"&gt;articles&lt;/a&gt;<br><br>In views.py as<br>reverse("someapp_name_namespace:articles")<br></td></tr></tbody></table>

 * ## Urls of Articles

     * ### Urls.py

       * /home/web\_dev/django\_basic\_documentation/basic\_django/articles/urls.py

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>from django.urls import path<br>from . import views<br><br>app_name='articles_app_name'<br><br>urlpatterns = [<br>    path('',views.articles, name='articles'),<br>]<br></td></tr></tbody></table>

     * ### \[image\]

       * ![](images/image57.png)

 * ## Urls of login\_register\_password

     * ### Urls.py

       * /home/web\_dev/django\_basic\_documentation/basic\_django/login\_register\_password/urls.py

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>from django.urls import path<br>from . import views<br><br>app_name='login_register_password_app_name'<br><br>urlpatterns = [<br>    path('user_login_via_otp_form_email',views.user_login_via_otp_form_email, name='user_login_via_otp_form_email'),<br>    path('user_login_via_otp_form_otp',views.user_login_via_otp_form_otp, name='user_login_via_otp_form_otp'),<br>    path('logout',views.logout_view, name='logout_view'),<br>]<br></td></tr></tbody></table>

     * ### \[image\]

       * ![](images/image95.png)

 * ## Urls of basic\_django

     * ### Urls.py

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>"""basic_django URL Configuration<br><br>The `urlpatterns` list routes URLs to views. For more information please see:<br>    https://docs.djangoproject.com/en/2.2/topics/http/urls/<br>Examples:<br>Function views<br>    1. Add an import:  from my_app import views<br>    2. Add a URL to urlpatterns:  path('', views.home, name='home')<br>Class-based views<br>    1. Add an import:  from other_app.views import Home<br>    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')<br>Including another URLconf<br>    1. Import the include() function: from django.urls import include, path<br>    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))<br>"""<br>from django.contrib import admin<br>from django.urls import path<br>from . import views<br>from django.urls import path, include<br><br>urlpatterns = [<br>    path('admin/', admin.site.urls),<br>    # this view is for testing 8commit related i.e sending email by gmail smtp<br>    path('test8commit',views.test_8commit, name='test_8commit'),<br>    # this view is for testing celery related by sending email<br>    path('celery_example_5commit',views.celery_example_5commit, name='celery_example_5commit'),<br>    # include all the urls from articles app<br>    path('', include('articles.urls',namespace='articles_namespace')),<br>    # include all the urls from login_register_password<br>    path('login_register_password/', include('login_register_password.urls',namespace='login_register_password_namespace')),<br>]<br></td></tr></tbody></table>

     * ### \[image\]

       * ![](images/image48.png)

     * ### \[image\] diff

       * ![](images/image162.png)

 * ## Forms: login\_register\_password

     * We will have mainly two forms 1) to fill email (UserLoginViaOtpFormEmail) and 2) to fill OTP (UserLoginViaOtpFormOTP) in the login\_register\_password app

     * Create a file forms.py (generally  is not created by default

     * ### Forms.py

       * /home/web\_dev/django\_basic\_documentation/basic\_django/login\_register\_password/forms.py

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>from custom_user.models import User<br>from django import forms<br>from basic_django import settings<br><br>class UserLoginViaOtpFormEmail(forms.ModelForm):<br>    class Meta:<br>        model = User<br>        fields = ['email']<br><br>    ############### important ################### <br>    # if we dont call clean. it<br>    #will check for unique instance clause for email  and gives User already exists:<br>    #go to: class BaseModelForm(BaseForm): --- self._validate_unique = False<br>    def clean(self):<br>        return self.cleaned_data<br><br>from django.core.validators  import RegexValidator<br>from django.utils.translation import ugettext_lazy as _<br>from django import forms<br><br>class UserLoginViaOtpFormOTP(forms.Form):<br><br>    otp_loginconfirm = forms.CharField(<br>                            help_text='Please Enter valid OTP sent to your Email', <br>                            label='Otp', <br>                            max_length=6,<br>                            validators=[RegexValidator(<br>                                        r'^\d{6}$',<br>                                        message=_('OTP shoud be of 6 digits'),<br>                                        code='invalid'<br>                                    )])<br><br></td></tr></tbody></table>

     * ### \[image\] (mainly for file location view)

       * ![](images/image139.png)

     * ### \[image\] forms.py code

       * ![](images/image70.png)

 * ## Views.py of login\_register\_password

     * Views.py is where we actually create the views. In the urls.py we have used these views

     * The following views are mentioned in the urls.py

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>urlpatterns = [<br>    path('user_login_via_otp_form_email',views.user_login_via_otp_form_email, name='user_login_via_otp_form_email'),<br>    path('user_login_via_otp_form_otp',views.user_login_via_otp_form_otp, name='user_login_via_otp_form_otp'),<br>    path('logout',views.logout_view, name='logout_view'),<br>]<br></td></tr></tbody></table>

     * ### Views.py

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>import jwt<br>import datetime<br>import pytz<br><br>from django.shortcuts import render, redirect<br>from django.http import HttpResponse<br>from basic_django import settings<br>from custom_user.models import User, UserSessionLog, ActionTypeForUserSessionLog<br>from django.utils.crypto import get_random_string<br>    <br>from django.template.loader import render_to_string<br>from .forms import UserLoginViaOtpFormEmail<br>from django.contrib import messages<br>from django.db.models.functions import Now<br>from django.utils.timezone import make_aware<br>from django.utils import timezone<br><br>from django.contrib.auth import authenticate<br>from django.contrib.auth import login<br>from django.contrib.auth import logout<br>from django.urls import reverse<br><br>def set_debug():<br>    import pudb;pudb.set_trace()<br><br># Create your views here.<br><br>###############################<br>## LOGGING<br>import logging<br>logger_custom_string = logging.getLogger("custom_string")<br>from basic_django import settings<br>#logger_custom_string.debug(settings.pp_odir(locals()))<br>#usage:<br>##logger_custom_string.debug(settings.pp_odir(user_set))  # This will pretty print all the properties from dir(user_set)<br>##logger_custom_string.debug(settings.pp_dict(user_set.__dict__))  # This will pretty print any dictionary<br>#sql = str(user_set.query)<br>#sql = user_set.query.__str__()<br>##logger_custom_string.debug(settings.pp_sql_sql(sql)) # pretty print the sql obtained from the .query<br>##logger_custom_string.debug(settings.pp_sql_query_pg(user_set)) # pretty print the sql using mogrify only possible with Psycopg<br>##logger_custom_string.debug(settings.pp_sql_query_any(user_set)) # pretty print the sql using EXPLAIN. But runs extra sql<br>#import traceback<br>##logger_custom_string.debug(settings.pp_traceback(traceback.format_stack())) #test traceback<br>logger_database = logging.getLogger("django.db.backends")<br>#usage:<br>#logger_database.filters[0].open()<br>#logger_database.filters[0].close()<br><br>from basic_django.tasks import send_email_task<br><br>def user_login_via_otp_form_email(request):<br><br>    ## CLEARING ALL THE MESSAGES<br>    system_messages = messages.get_messages(request)<br>    for message in system_messages:<br>        # This iteration is necessary<br>        pass<br>    system_messages.used = True<br><br>    # TRYING to check if email is there in session.we want to delete it<br>    try:<br>        del request.session['email']<br>    except:<br>        pass<br><br>    try:<br>        del request.session['otp_modified_date_loginconfirm']<br>    except:<br>        pass<br><br><br>    #request.session.modified = True<br>    if request.method == 'POST':<br>        form = UserLoginViaOtpFormEmail(request.POST)<br>        if form.is_valid():<br>            email = form.cleaned_data.get('email')<br>            # generate a random pin using crpto functions<br>            pin = get_random_string(length=6, allowed_chars='1234567890')<br>            <br>            # EMAIL subject and BODY<br>            # for BODY we use a template and render it with parameters<br>            subject = pin + ': To Login via OTP'<br>            # We to create the email body. So we create a template and pass the required arguments.<br>            # render_to_string will render the template with the context values<br>            message = render_to_string('login_register_password/login_via_otp/email/login_otp_sendemail.html', {<br>                'email': email,<br>                'pin': pin<br>            })<br><br>            # USING CELERY TASK for sending email Asynchronously<br>            #match.email_user(subject, message). This will delay the response <br>            # So will do this task asynchronously using celery<br>            # We have created a celery task. Using it we will send the email.<br>            # The code does not have to wait till the email is sent<br>            send_email_task.delay(email,subject,message)<br><br>            #USING MESSAGES to inform the user in the next page about email is being sent<br>            #we want to inform the user on the next page that email is being sent for OTP<br>            #For this we use messages<br>            messages.success(request, 'Email is being sent please check')<br><br>            payload = {<br>                'email': email,<br>                'OTP': pin,<br>                'creation_time': str(datetime.datetime.now(tz=pytz.timezone('UTC')).isoformat())<br>            }<br><br>            jwt_token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256').decode('utf-8')<br>            # USING SESSION to make data available to next view.<br>            #For the next page we want to send some data which we dont want to display.<br>            request.session['jwt_token'] = jwt_token<br>            #logger_custom_string.debug(jwt_token)<br><br>            # REDIRECTING TO A DIFFERENT VIEW ie. different URL<br>            return redirect('login_register_password_namespace:user_login_via_otp_form_otp')<br>    else:<br>        form = UserLoginViaOtpFormEmail(initial={'email': settings.TESTING_EMAIL})<br>        <br>    return render(request, 'login_register_password/login_via_otp/user_login_via_otp_form_email.html', {'form': form})<br><br><br><br><br>def user_login_via_otp_form_otp(request):<br>    ## CLEARING ALL THE MESSAGES<br>    system_messages = messages.get_messages(request)<br>    for message in system_messages:<br>        # This iteration is necessary<br>        pass<br>    system_messages.used = True<br><br><br>    # CHECKING whether the session variable exists or not<br>    if 'jwt_token' in request.session:<br>        jwt_token = request.session['jwt_token']<br>    else:<br>        messages.error(request, 'jwt_token in session not found')<br>        return redirect('login_register_password_namespace:user_login_via_otp_form_email')<br><br>    # CHECKING jwt token and getting the payload<br>    try:<br>        # options = {<br>        #     'verify_exp': True,<br>        # }<br>        payload = jwt.decode(<br>            jwt_token,<br>            settings.SECRET_KEY,<br>            True,<br>            #options=options,<br>        )<br>        #logger_custom_string.debug(settings.pp_dict(payload))<br>    except Exception as e:  # NoQA<br>        #logger_custom_string.debug(str(e))<br>        pass<br><br>    # FORM<br>    from .forms import UserLoginViaOtpFormOTP<br>    if request.method == 'POST':<br><br>        form = UserLoginViaOtpFormOTP(request.POST)<br>        if form.is_valid():<br>            otp_loginconfirm = form.cleaned_data.get('otp_loginconfirm')<br><br>            #COMPARE TIME LIMIT FOR OTP<br><br>            #convert payload creation time to datetime<br>            creation_time = datetime.datetime.fromisoformat(payload['creation_time'])<br>            #datetime.timedelta(minutes=1, seconds=1)<br>            timelimit = datetime.timedelta(seconds=10)<br>            current_time = datetime.datetime.now(tz=pytz.timezone('UTC'))<br>            timecheck = current_time - creation_time &lt; timelimit<br>            timedelta = current_time - creation_time<br>            logger_custom_string.debug(settings.pp_odir(locals()))<br><br>            if current_time - creation_time &gt; timelimit:<br>                form.add_error(None,"OTP expired, Click on resend OTP")<br>                return render(request, 'login_register_password/login_via_otp/user_login_via_otp_form_otp.html',{'form': form})<br><br>            if payload['OTP'] == otp_loginconfirm:<br><br>                # CHECK for an existing user<br>                try:<br><br>                    match = User.objects.get(email=payload['email'])<br>                    time_now = timezone.now()<br>                    # if we do timezone.now(), (with a comma then it will save as tuple and will give error)<br>                    match.last_login2=time_now<br>                    match.recentdate_login_via_otp=time_now<br>                    match.save()<br><br>                    if match.is_active:<br>                        login(request,match,backend='django.contrib.auth.backends.ModelBackend')<br>                    else:<br>                        messages(email, ' :not active')<br>                        return redirect('login_register_password_namespace:user_login_via_otp_form_email')<br><br>                    #Get ip address<br>                    ip = settings.get_client_ip(request)<br><br>                    # get the action type<br>                    action_type = ActionTypeForUserSessionLog.objects.get(action='login_by_otp')<br><br>                    # Save in the session<br>                    match_UserSessionLog = UserSessionLog(<br>                        user_email=match.email,<br>                        ip_address = ip,<br>                        user = match,<br>                        otp_used_for_otplogin=payload['OTP'],<br>                        action_type=action_type,<br>                        device_type=request.META['HTTP_USER_AGENT'],<br>                        created_time=time_now<br>                    )<br><br>                    match_UserSessionLog.save()<br>                    <br>                except User.DoesNotExist:<br>                    #we create a new user<br><br>                        ###   total length of Model_meta.get_fields(include_hidden=True):  31<br>                        ###   <br>                        ###   <br>                        ###   [<br>                        ###       "&lt;ManyToOneRel: admin.logentry&gt;",<br>                        ###       "&lt;ManyToOneRel: custom_user.user_groups&gt;",<br>                        ###       "&lt;ManyToOneRel: custom_user.user_user_permissions&gt;",<br>                        ###       "&lt;ManyToOneRel: custom_user.usersessionlog&gt;",<br>                        ###       [<br>                        ###           "&lt;django.db.models.fields.AutoField: id&gt;",<br>                        ###           "STR: custom_user.User.id"<br>                        ###       ],<br>                        ###       [<br>                        ###           "&lt;django.db.models.fields.DateTimeField: last_login&gt;",<br>                        ###           "STR: custom_user.User.last_login"<br>                        ###       ],<br>                        ###       [<br>                        ###           "&lt;django.db.models.fields.BooleanField: is_superuser&gt;",<br>                        ###           "STR: custom_user.User.is_superuser"<br>                        ###       ],<br>                        ###       [<br>                        ###           "&lt;django.db.models.fields.BooleanField: is_staff&gt;",<br>                        ###           "STR: custom_user.User.is_staff"<br>                        ###       ],<br>                        ###       [<br>                        ###           "&lt;django.db.models.fields.DateTimeField: date_joined&gt;",<br>                        ###           "STR: custom_user.User.date_joined"<br>                        ###       ],<br>                        ###       [<br>                        ###           "&lt;django.db.models.fields.CharField: password&gt;",<br>                        ###           "STR: custom_user.User.password"<br>                        ###       ],<br>                        ###       [<br>                        ###           "&lt;django.db.models.fields.DateTimeField: recentdate_login_via_passwd&gt;",<br>                        ###           "STR: custom_user.User.recentdate_login_via_passwd"<br>                        ###       ],<br>                        ###       [<br>                        ###           "&lt;django.db.models.fields.DateTimeField: recentdate_login_via_otp&gt;",<br>                        ###           "STR: custom_user.User.recentdate_login_via_otp"<br>                        ###       ],<br>                        ###       [<br>                        ###           "&lt;django.db.models.fields.DateTimeField: recentdate_password_change&gt;",<br>                        ###           "STR: custom_user.User.recentdate_password_change"<br>                        ###       ],<br>                        ###       [<br>                        ###           "&lt;django.db.models.fields.CharField: first_name&gt;",<br>                        ###           "STR: custom_user.User.first_name"<br>                        ###       ],<br>                        ###       [<br>                        ###           "&lt;django.db.models.fields.CharField: last_name&gt;",<br>                        ###           "STR: custom_user.User.last_name"<br>                        ###       ],<br>                        ###       [<br>                        ###           "&lt;django.db.models.fields.EmailField: email&gt;",<br>                        ###           "STR: custom_user.User.email"<br>                        ###       ],<br>                        ###       [<br>                        ###           "&lt;django.db.models.fields.BooleanField: is_active&gt;",<br>                        ###           "STR: custom_user.User.is_active"<br>                        ###       ],<br>                        ###       [<br>                        ###           "&lt;django.db.models.fields.CharField: recent_otp_used_for_pass_change&gt;",<br>                        ###           "STR: custom_user.User.recent_otp_used_for_pass_change"<br>                        ###       ],<br>                        ###       [<br>                        ###           "&lt;django.db.models.fields.DateTimeField: date_of_recent_otp_used_for_pass_change&gt;",<br>                        ###           "STR: custom_user.User.date_of_recent_otp_used_for_pass_change"<br>                        ###       ],<br>                        ###       [<br>                        ###           "&lt;django.db.models.fields.CharField: otp_used_while_passlogin_create&gt;",<br>                        ###           "STR: custom_user.User.otp_used_while_passlogin_create"<br>                        ###       ],<br>                        ###       [<br>                        ###           "&lt;django.db.models.fields.DateTimeField: date_of_otp_used_while_passlogin_create&gt;",<br>                        ###           "STR: custom_user.User.date_of_otp_used_while_passlogin_create"<br>                        ###       ],<br>                        ###       [<br>                        ###           "&lt;django.db.models.fields.CharField: first_otp_used_for_otplogin&gt;",<br>                        ###           "STR: custom_user.User.first_otp_used_for_otplogin"<br>                        ###       ],<br>                        ###       [<br>                        ###           "&lt;django.db.models.fields.DateTimeField: date_of_first_otp_used_for_otplogin&gt;",<br>                        ###           "STR: custom_user.User.date_of_first_otp_used_for_otplogin"<br>                        ###       ],<br>                        ###       [<br>                        ###           "&lt;django.db.models.fields.TextField: about&gt;",<br>                        ###           "STR: custom_user.User.about"<br>                        ###       ],<br>                        ###       [<br>                        ###           "&lt;django.db.models.fields.CharField: location&gt;",<br>                        ###           "STR: custom_user.User.location"<br>                        ###       ],<br>                        ###       [<br>                        ###           "&lt;django.db.models.fields.DateField: birth_date&gt;",<br>                        ###           "STR: custom_user.User.birth_date"<br>                        ###       ],<br>                        ###       [<br>                        ###           "&lt;django.db.models.fields.DateTimeField: modified_date&gt;",<br>                        ###           "STR: custom_user.User.modified_date"<br>                        ###       ],<br>                        ###       [<br>                        ###           "&lt;django.db.models.fields.DateTimeField: creation_date&gt;",<br>                        ###           "STR: custom_user.User.creation_date"<br>                        ###       ],<br>                        ###       [<br>                        ###           "&lt;django.db.models.fields.DateTimeField: last_login2&gt;",<br>                        ###           "STR: custom_user.User.last_login2"<br>                        ###       ],<br>                        ###       [<br>                        ###           "&lt;django.db.models.fields.related.ManyToManyField: groups&gt;",<br>                        ###           "STR: custom_user.User.groups"<br>                        ###       ],<br>                        ###       [<br>                        ###           "&lt;django.db.models.fields.related.ManyToManyField: user_permissions&gt;",<br>                        ###           "STR: custom_user.User.user_permissions"<br>                        ###       ]<br>                        ###   ]<br>                        ###   <br>                        ###   <br>                        ###   <br>                        ###   Lenght of c_dict[000_null_true***********************************************************************]  8<br>                        ###   Lenght of c_dict[001_remaining***********************************************************************]  1<br>                        ###   Lenght of c_dict[002_null_false_and_empty_strings****************************************************]  10<br>                        ###   Lenght of c_dict[003_auto_now_add__OR__auto_now******************************************************]  2<br>                        ###   Lenght of c_dict[004_auto_created********************************************************************]  5<br>                        ###   Lenght of c_dict[005_default_not_empty_string********************************************************]  5<br>                        ###   Total lenght of c_dict:  31<br>                        ###   {<br>                        ###       "000_null_true***********************************************************************": {<br>                        ###           "birth_date": {<br>                        ###               "000_class": "&lt;class 'django.db.models.fields.DateField'&gt;",<br>                        ###               "005_null": true,<br>                        ###               "006_empty_strings_allowed": false,<br>                        ###               "007_blank": true<br>                        ###           },<br>                        ###@@@@       "date_of_first_otp_used_for_otplogin": {<br>                        ###               "000_class": "&lt;class 'django.db.models.fields.DateTimeField'&gt;",<br>                        ###               "005_null": true,<br>                        ###               "006_empty_strings_allowed": false,<br>                        ###               "007_blank": false<br>                        ###           },<br>                        ###           "date_of_otp_used_while_passlogin_create": {<br>                        ###               "000_class": "&lt;class 'django.db.models.fields.DateTimeField'&gt;",<br>                        ###               "005_null": true,<br>                        ###               "006_empty_strings_allowed": false,<br>                        ###               "007_blank": false<br>                        ###           },<br>                        ###           "date_of_recent_otp_used_for_pass_change": {<br>                        ###               "000_class": "&lt;class 'django.db.models.fields.DateTimeField'&gt;",<br>                        ###               "005_null": true,<br>                        ###               "006_empty_strings_allowed": false,<br>                        ###               "007_blank": false<br>                        ###           },<br>                        ###           "last_login": {<br>                        ###               "000_class": "&lt;class 'django.db.models.fields.DateTimeField'&gt;",<br>                        ###               "005_null": true,<br>                        ###               "006_empty_strings_allowed": false,<br>                        ###               "007_blank": true<br>                        ###           },<br>                        ###@@@@       "recentdate_login_via_otp": {<br>                        ###               "000_class": "&lt;class 'django.db.models.fields.DateTimeField'&gt;",<br>                        ###               "005_null": true,<br>                        ###               "006_empty_strings_allowed": false,<br>                        ###               "007_blank": true<br>                        ###           },<br>                        ###           "recentdate_login_via_passwd": {<br>                        ###               "000_class": "&lt;class 'django.db.models.fields.DateTimeField'&gt;",<br>                        ###               "005_null": true,<br>                        ###               "006_empty_strings_allowed": false,<br>                        ###               "007_blank": true<br>                        ###           },<br>                        ###           "recentdate_password_change": {<br>                        ###               "000_class": "&lt;class 'django.db.models.fields.DateTimeField'&gt;",<br>                        ###               "005_null": true,<br>                        ###               "006_empty_strings_allowed": false,<br>                        ###               "007_blank": true<br>                        ###           }<br>                        ###       },<br>                        ###       "001_remaining***********************************************************************": {<br>                        ###@@@@       "last_login2": {<br>                        ###               "000_class": "&lt;class 'django.db.models.fields.DateTimeField'&gt;",<br>                        ###               "005_null": false,<br>                        ###               "006_empty_strings_allowed": false,<br>                        ###               "007_blank": true<br>                        ###           }<br>                        ###       },<br>                        ###       "002_null_false_and_empty_strings****************************************************": {<br>                        ###           "about": {<br>                        ###               "000_class": "&lt;class 'django.db.models.fields.TextField'&gt;",<br>                        ###               "001_default": "",<br>                        ###               "005_null": false,<br>                        ###               "006_empty_strings_allowed": true,<br>                        ###               "007_blank": true,<br>                        ###               "max_length": 500<br>                        ###           },<br>                        ###@@@@       "email": {<br>                        ###               "000_class": "&lt;class 'django.db.models.fields.EmailField'&gt;",<br>                        ###               "001_default": "",<br>                        ###               "005_null": false,<br>                        ###               "006_empty_strings_allowed": true,<br>                        ###               "007_blank": false,<br>                        ###               "max_length": 254,<br>                        ###               "unique": true<br>                        ###           },<br>                        ###           "first_name": {<br>                        ###               "000_class": "&lt;class 'django.db.models.fields.CharField'&gt;",<br>                        ###               "001_default": "",<br>                        ###               "005_null": false,<br>                        ###               "006_empty_strings_allowed": true,<br>                        ###               "007_blank": true,<br>                        ###               "max_length": 30<br>                        ###           },<br>                        ###@@@@       "first_otp_used_for_otplogin": {<br>                        ###               "000_class": "&lt;class 'django.db.models.fields.CharField'&gt;",<br>                        ###               "001_default": "",<br>                        ###               "005_null": false,<br>                        ###               "006_empty_strings_allowed": true,<br>                        ###               "007_blank": false,<br>                        ###               "max_length": 6<br>                        ###           },<br>                        ###           "groups": {<br>                        ###               "000_class": "&lt;class 'django.db.models.fields.related.ManyToManyField'&gt;",<br>                        ###               "001_default": "",<br>                        ###               "005_null": false,<br>                        ###               "006_empty_strings_allowed": true,<br>                        ###               "007_blank": true,<br>                        ###               "many_to_many": true,<br>                        ###               "one_to_many": false,<br>                        ###               "one_to_one": false,<br>                        ###               "remote_field": "&lt;ManyToManyRel: custom_user.user&gt;"<br>                        ###           },<br>                        ###           "last_name": {<br>                        ###               "000_class": "&lt;class 'django.db.models.fields.CharField'&gt;",<br>                        ###               "001_default": "",<br>                        ###               "005_null": false,<br>                        ###               "006_empty_strings_allowed": true,<br>                        ###               "007_blank": true,<br>                        ###               "max_length": 150<br>                        ###           },<br>                        ###           "location": {<br>                        ###               "000_class": "&lt;class 'django.db.models.fields.CharField'&gt;",<br>                        ###               "001_default": "",<br>                        ###               "005_null": false,<br>                        ###               "006_empty_strings_allowed": true,<br>                        ###               "007_blank": true,<br>                        ###               "max_length": 30<br>                        ###           },<br>                        ###           "otp_used_while_passlogin_create": {<br>                        ###               "000_class": "&lt;class 'django.db.models.fields.CharField'&gt;",<br>                        ###               "001_default": "",<br>                        ###               "005_null": false,<br>                        ###               "006_empty_strings_allowed": true,<br>                        ###               "007_blank": false,<br>                        ###               "max_length": 6<br>                        ###           },<br>                        ###           "recent_otp_used_for_pass_change": {<br>                        ###               "000_class": "&lt;class 'django.db.models.fields.CharField'&gt;",<br>                        ###               "001_default": "",<br>                        ###               "005_null": false,<br>                        ###               "006_empty_strings_allowed": true,<br>                        ###               "007_blank": false,<br>                        ###               "max_length": 6<br>                        ###           },<br>                        ###           "user_permissions": {<br>                        ###               "000_class": "&lt;class 'django.db.models.fields.related.ManyToManyField'&gt;",<br>                        ###               "001_default": "",<br>                        ###               "005_null": false,<br>                        ###               "006_empty_strings_allowed": true,<br>                        ###               "007_blank": true,<br>                        ###               "many_to_many": true,<br>                        ###               "one_to_many": false,<br>                        ###               "one_to_one": false,<br>                        ###               "remote_field": "&lt;ManyToManyRel: custom_user.user&gt;"<br>                        ###           }<br>                        ###       },<br>                        ###       "003_auto_now_add__OR__auto_now******************************************************": {<br>                        ###           "creation_date": {<br>                        ###               "000_class": "&lt;class 'django.db.models.fields.DateTimeField'&gt;",<br>                        ###               "003_auto_now_add": true,<br>                        ###               "005_null": false,<br>                        ###               "006_empty_strings_allowed": false,<br>                        ###               "007_blank": true,<br>                        ###               "editable": false<br>                        ###           },<br>                        ###           "modified_date": {<br>                        ###               "000_class": "&lt;class 'django.db.models.fields.DateTimeField'&gt;",<br>                        ###               "004_auto_now": true,<br>                        ###               "005_null": false,<br>                        ###               "006_empty_strings_allowed": false,<br>                        ###               "007_blank": true,<br>                        ###               "editable": false<br>                        ###           }<br>                        ###       },<br>                        ###       "004_auto_created********************************************************************": {<br>                        ###           "User_groups+": {<br>                        ###               "000_class": "&lt;class 'django.db.models.fields.reverse_related.ManyToOneRel'&gt;",<br>                        ###               "002_auto_created": true,<br>                        ###               "005_null": true,<br>                        ###               "editable": false,<br>                        ###               "hidden": true,<br>                        ###               "many_to_many": false,<br>                        ###               "one_to_many": true,<br>                        ###               "one_to_one": false,<br>                        ###               "remote_field": [<br>                        ###                   "&lt;django.db.models.fields.related.ForeignKey: user&gt;",<br>                        ###                   "STR: custom_user.User_groups.user"<br>                        ###               ]<br>                        ###           },<br>                        ###           "User_user_permissions+": {<br>                        ###               "000_class": "&lt;class 'django.db.models.fields.reverse_related.ManyToOneRel'&gt;",<br>                        ###               "002_auto_created": true,<br>                        ###               "005_null": true,<br>                        ###               "editable": false,<br>                        ###               "hidden": true,<br>                        ###               "many_to_many": false,<br>                        ###               "one_to_many": true,<br>                        ###               "one_to_one": false,<br>                        ###               "remote_field": [<br>                        ###                   "&lt;django.db.models.fields.related.ForeignKey: user&gt;",<br>                        ###                   "STR: custom_user.User_user_permissions.user"<br>                        ###               ]<br>                        ###           },<br>                        ###           "id": {<br>                        ###               "000_class": "&lt;class 'django.db.models.fields.AutoField'&gt;",<br>                        ###               "002_auto_created": true,<br>                        ###               "005_null": false,<br>                        ###               "006_empty_strings_allowed": false,<br>                        ###               "007_blank": true,<br>                        ###               "primary_key": true,<br>                        ###               "unique": true<br>                        ###           },<br>                        ###           "logentry": {<br>                        ###               "000_class": "&lt;class 'django.db.models.fields.reverse_related.ManyToOneRel'&gt;",<br>                        ###               "002_auto_created": true,<br>                        ###               "005_null": true,<br>                        ###               "editable": false,<br>                        ###               "many_to_many": false,<br>                        ###               "one_to_many": true,<br>                        ###               "one_to_one": false,<br>                        ###               "remote_field": [<br>                        ###                   "&lt;django.db.models.fields.related.ForeignKey: user&gt;",<br>                        ###                   "STR: admin.LogEntry.user"<br>                        ###               ]<br>                        ###           },<br>                        ###           "usersessionlog": {<br>                        ###               "000_class": "&lt;class 'django.db.models.fields.reverse_related.ManyToOneRel'&gt;",<br>                        ###               "002_auto_created": true,<br>                        ###               "005_null": true,<br>                        ###               "editable": false,<br>                        ###               "many_to_many": false,<br>                        ###               "one_to_many": true,<br>                        ###               "one_to_one": false,<br>                        ###               "remote_field": [<br>                        ###                   "&lt;django.db.models.fields.related.ForeignKey: user&gt;",<br>                        ###                   "STR: custom_user.UserSessionLog.user"<br>                        ###               ]<br>                        ###           }<br>                        ###       },<br>                        ###       "005_default_not_empty_string********************************************************": {<br>                        ###@@@@       "date_joined": {<br>                        ###               "000_class": "&lt;class 'django.db.models.fields.DateTimeField'&gt;",<br>                        ###               "001_default": [<br>                        ###                   "datetime.datetime(2019, 10, 12, 1, 16, 2, 339774, tzinfo=&lt;UTC&gt;)",<br>                        ###                   "STR: 2019-10-12 01:16:02.339774+00:00"<br>                        ###               ],<br>                        ###               "005_null": false,<br>                        ###               "006_empty_strings_allowed": false,<br>                        ###               "007_blank": false<br>                        ###           },<br>                        ###@@@@       "is_active": {<br>                        ###               "000_class": "&lt;class 'django.db.models.fields.BooleanField'&gt;",<br>                        ###               "001_default": false,<br>                        ###               "005_null": false,<br>                        ###               "006_empty_strings_allowed": false,<br>                        ###               "007_blank": false<br>                        ###           },<br>                        ###           "is_staff": {<br>                        ###               "000_class": "&lt;class 'django.db.models.fields.BooleanField'&gt;",<br>                        ###               "001_default": false,<br>                        ###               "005_null": false,<br>                        ###               "006_empty_strings_allowed": false,<br>                        ###               "007_blank": false<br>                        ###           },<br>                        ###           "is_superuser": {<br>                        ###               "000_class": "&lt;class 'django.db.models.fields.BooleanField'&gt;",<br>                        ###               "001_default": false,<br>                        ###               "005_null": false,<br>                        ###               "006_empty_strings_allowed": false,<br>                        ###               "007_blank": false<br>                        ###           },<br>                        ###           "password": {<br>                        ###               "000_class": "&lt;class 'django.db.models.fields.CharField'&gt;",<br>                        ###               "001_default": "pbkdf2_sha256$150000$zV7im78Gkp9T$zv2vl1sYuqtAaoWhjn7jpdHIoY2mzFKrtsN9MiR37SQ=",<br>                        ###               "005_null": false,<br>                        ###               "006_empty_strings_allowed": true,<br>                        ###               "007_blank": false,<br>                        ###               "max_length": 128<br>                        ###           }<br>                        ###       }<br>                        ###   }<br><br>                    time_now = timezone.now()<br>                    # if we do timezone.now(), (with a comma then it will save as tuple and will give error)<br>                    newuser = User(<br>                        email=payload['email'],<br>                        first_otp_used_for_otplogin=payload['OTP'],<br>                        date_of_first_otp_used_for_otplogin=time_now,<br>                        last_login2=time_now,<br>                        recentdate_login_via_otp=time_now,<br>                        is_active=True,<br>                        # we use timezone.now without brackets in default, so if dont convert to string it throws error<br>                        # expected string or bytes-like object @ dateparse.py in parse_datetime, line 106<br>                        date_joined=time_now<br>                        )<br>                    newuser.save()<br><br>                    if newuser.is_active:<br>                        login(request,newuser,backend='django.contrib.auth.backends.ModelBackend')<br>                    else:<br>                        messages(email, ' :not active')<br>                        return redirect('login_register_password_namespace:user_login_via_otp_form_email')<br><br><br>                    # Get the client ip:<br>                    ip = settings.get_client_ip(request)<br><br>                    action_type = ActionTypeForUserSessionLog.objects.get(action='login_by_otp')<br><br><br><br>                    # Save in the session<br>                    new_UserSessionLog = UserSessionLog(<br>                        user_email=newuser.email,<br>                        ip_address = ip,<br>                        user = newuser,<br>                        otp_used_for_otplogin=payload['OTP'],<br>                        action_type=action_type,<br>                        device_type=request.META['HTTP_USER_AGENT'],<br>                        created_time=time_now<br>                    )<br><br>                    new_UserSessionLog.save()<br><br>                messages.success(request, 'Login successful')<br>                return redirect('articles_namespace:articles')<br><br>            form.add_error(None,"Form Error: Wrong OTP entered")<br>            return render(request, 'login_register_password/login_via_otp/user_login_via_otp_form_otp.html',{'form': form})<br>    else:<br>        #logger_custom_string.debug(request.GET.get('resendotp'))<br>        #logger_custom_string.debug(settings.pp_dict(request.GET))<br>        #logger_custom_string.debug('resendotp' in request.GET)<br><br>        if 'resendotp' in request.GET:<br><br>            email = payload['email']<br>            # generate a random pin using crpto functions<br>            pin = get_random_string(length=6, allowed_chars='1234567890')<br>            <br>            # EMAIL subject and BODY<br>            # for BODY we use a template and render it with parameters<br>            subject = pin + ': To Login via OTP'<br>            # We to create the email body. So we create a template and pass the required arguments.<br>            # render_to_string will render the template with the context values<br>            message = render_to_string('login_register_password/login_via_otp/email/login_otp_sendemail.html', {<br>                'email': email,<br>                'pin': pin<br>            })<br><br>            # USING CELERY TASK for sending email Asynchronously<br>            #match.email_user(subject, message). This will delay the response <br>            # So will do this task asynchronously using celery<br>            # We have created a celery task. Using it we will send the email.<br>            # The code does not have to wait till the email is sent<br>            send_email_task.delay(email,subject,message)<br><br>            #USING MESSAGES to inform the user in the next page about email is being sent<br>            #we want to inform the user on the next page that email is being sent for OTP<br>            #For this we use messages<br>            messages.success(request, 'Email is being sent please check')<br><br>            payload = {<br>                'email': email,<br>                'OTP': pin,<br>                'creation_time': str(datetime.datetime.now(tz=pytz.timezone('UTC')).isoformat())<br>            }<br><br>            jwt_token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256').decode('utf-8')<br>            # USING SESSION to make data available to next view.<br>            #For the next page we want to send some data which we dont want to display.<br>            request.session['jwt_token'] = jwt_token<br>            #logger_custom_string.debug(jwt_token)<br><br>        else:<br>            # Want to check no one access this page directy. But only through the user_login_via_otp_form_email pages<br>            try:<br>                prev_url = request.META['HTTP_REFERER']<br><br>                # we want to get the url from namespace . We use reverse. But this give relative url not the full url with domain<br>                login_form_email_url_reverse = reverse("login_register_password_namespace:user_login_via_otp_form_email")<br>                # to get the full url we have to use do the below<br>                login_form_email_url_reverse_full = request.build_absolute_uri(login_form_email_url_reverse)<br><br>                #logger_custom_string.debug(prev_url)<br>                #logger_custom_string.debug(login_form_email_url_reverse_full)<br>                if prev_url != login_form_email_url_reverse_full:<br>                    #logger_custom_string.debug(prev_url != login_form_email_url_reverse_full)<br>                    return redirect('login_register_password_namespace:user_login_via_otp_form_email')<br>            except Exception as e:<br>                messages.error(request, str(e))<br>                #logger_custom_string.debug(str(e))<br>                return redirect('login_register_password_namespace:user_login_via_otp_form_email')<br><br>        form = UserLoginViaOtpFormOTP(initial={'otp_loginconfirm': payload['OTP']})<br>    return render(request, 'login_register_password/login_via_otp/user_login_via_otp_form_otp.html',{'form': form})<br><br><br>def logout_view(request):<br>    # never use the same name as logout(request) it will cause recurssion error<br>    email = request.user.email<br>    logout(request)<br><br>    ## CLEARING ALL THE MESSAGES<br>    system_messages = messages.get_messages(request)<br>    for message in system_messages:<br>        # This iteration is necessary<br>        pass<br>    system_messages.used = True<br>    messages.success(request, email + ' has logged out successfully')<br>    return redirect('articles_namespace:articles')<br><br></td></tr></tbody></table>

     * ### \[image\] \[file location view\]

       * ![](images/image148.png)

     * ### \[image\] code view

       * ![](images/image159.png)![](images/image128.png)![](images/image182.png)![](images/image136.png)![](images/image101.png)![](images/image46.png)![](images/image133.png)![](images/image38.png)![](images/image111.png)![](images/image155.png)![](images/image156.png)![](images/image168.png)![](images/image173.png)![](images/image216.png)![](images/image192.png)![](images/image225.png)![](images/image239.png)![](images/image17.png)![](images/image26.png)![](images/image131.png)![](images/image106.png)![](images/image122.png)![](images/image25.png)![](images/image66.png)![](images/image89.png)![](images/image191.png)![](images/image35.png)

     * ### Views of articles.py

       * Urls of articles.py

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>urlpatterns = [<br>    path('',views.articles, name='articles'),<br>]<br></td></tr></tbody></table>

     * ### Views.py

       * /home/web\_dev/django\_basic\_documentation/basic\_django/articles/views.py

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>from django.shortcuts import render<br>from django.contrib.auth import logout<br>from django.contrib import messages<br><br># Create your views here.<br><br>def articles(request):<br>        return render(request, 'articles/main_page/articles.html')<br></td></tr></tbody></table>

     * ### \[image\] code

       * ![](images/image113.png)

 * ## Celery tasks for sending emails:

     * Since we have to send OTP and we dont want it to block the User experience we use celery.

     * Since sending email will be general task related it will be defind in the basic\_django/tasks.py

     * It is already defined in Celery section.

     * ### \[code\]

       * /home/web\_dev/django\_basic\_documentation/basic\_django/basic\_django/tasks.py

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>from basic_django import celery_app<br>from django.core.mail import send_mail<br><br>@celery_app.task<br>def send_email_task(email,subject,message):<br>    send_mail(subject, message,None,[email])<br>    logger_custom_string.debug("Email Sent")<br></td></tr></tbody></table>

 * ## Request.SESSION: for passing making data available to next view.

     * To pass data from one view to another the best way is to 

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>In the current view define the session variable<br>request.session['email'] = 'something'<br><br>In the next view access the session variable using<br>if 'email' in request.session:<br>    variable = request.session['email']<br></td></tr></tbody></table>

 * ## PYTHON: RuntimeWarning: DateTimeField received a naive datetime while time zone support is active. RuntimeWarning)

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>a naive DateTimeField object:<br>&gt;&gt;&gt; from datetime import datetime<br>&gt;&gt;&gt; datetime.now()<br>datetime.datetime(2013, 11, 20, 20, 9, 26, 423063)<br><br>https://stackoverflow.com/a/45080605/2897115<br>Use django.utils.timezone.make_aware function to make your naive datetime objects timezone aware and avoid those warnings.<br><br>It converts naive datetime object (without timezone info) to the one that has timezone info (using timezone specified in your django settings if you don't specify it explicitly as a second argument):<br><br>import datetime<br>from django.conf import settings<br>from django.utils.timezone import make_aware<br><br>naive_datetime = datetime.datetime.now()<br>naive_datetime.tzinfo  # None<br><br>settings.TIME_ZONE  # 'UTC'<br>aware_datetime = make_aware(naive_datetime)<br>aware_datetime.tzinfo  # &lt;UTC&gt;<br></td></tr></tbody></table>

 * ## Form \> View \> html

     * The sequence of creating any page is generally first we define a form and then create a view and using that form then create html

 * ## Create a Form for login via OTP

     * /home/web\_dev/django\_basic\_documentation/basic\_django/login\_register\_password/forms.py

     * Here we create two forms: UserLoginViaOtpFormEmail and UserLoginViaOtpFormOTP

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>from custom_user.models import User<br>from django import forms<br>from basic_django import settings<br><br>###############################<br>## LOGGING<br>import logging<br>logger_custom_string = logging.getLogger("custom_string")<br>from basic_django import settings<br>#usage:<br>#logger_custom_string.debug("ANY STRING")<br>#logger_custom_string.debug(settings.pp_odir(user_set))  # This will pretty print all the properties from dir(user_set)<br>#logger_custom_string.debug(settings.pp_dict(user_set.__dict__))  # This will pretty print any dictionary<br>#sql = str(user_set.query)<br>#sql = user_set.query.__str__()<br>#logger_custom_string.debug(settings.pp_sql_sql(sql)) # pretty print the sql obtained from the .query<br>#logger_custom_string.debug(settings.pp_sql_query_pg(user_set)) # pretty print the sql using mogrify only possible with Psycopg<br>#logger_custom_string.debug(settings.pp_sql_query_any(user_set)) # pretty print the sql using EXPLAIN. But runs extra sql<br>logger_database = logging.getLogger("django.db.backends")<br>#usage:<br>#logger_database.filters[0].open()<br>#logger_database.filters[0].close()<br><br><br><br>class UserLoginViaOtpFormEmail(forms.ModelForm):<br>    """<br>    Base class for authenticating users. Extend this to get a form that accepts<br>    username/password logins.<br>    """<br>    class Meta:<br>        model = User<br>        fields = ['email']<br><br>    def clean_email(self):<br>        # Get the email<br>        email = self.cleaned_data.get('email').lower()<br><br>        # Check to see if any users already exist with this email as a username.<br>        try:<br>            match = User.objects.get(email=email)<br>            logger_custom_string.debug(settings.pp_odir(match))<br>            if match.last_login_otp == None:<br>                match.delete()<br>            else:<br>                if not match.is_active:<br>                    raise forms.ValidationError('This email address not active contact the admin')<br>        except User.DoesNotExist:<br>            pass<br>            # Unable to find a user, this is fine<br><br>        return email<br><br>    ############### important ################### <br>    # if we dont call clean. it<br>    #will check for unique instance clause for email  and gives User already exists:<br>    #go to: class BaseModelForm(BaseForm): --- self._validate_unique = False<br>    def clean(self):<br>        return self.cleaned_data<br><br>    def save(self, commit=True):<br>            user = super().save(commit=False)<br>            if commit:<br>                user.save()<br>            return user<br><br><br><br>class UserLoginViaOtpFormOTP(forms.ModelForm):<br>    class Meta:<br>        model = User     ##if we use model for then dont forget to use def clean(self): else it will check for uniques values<br>        fields = ['email','otp_loginconfirm']<br><br>    def __init__(self, *args, **kwargs):<br>        super().__init__(*args, **kwargs)<br>        self.fields['email'].widget = forms.HiddenInput()<br></td></tr></tbody></table>

     * /home/web\_dev/django\_basic\_documentation/basic\_django/login\_register\_password/views.py

     * Here we create two views: user\_login\_via\_otp\_form\_email (redirects to) user\_login\_via\_otp\_form\_otp

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>from django.shortcuts import render, redirect<br>from django.http import HttpResponse<br>from basic_django import settings<br>from custom_user.models import User<br>from django.utils.crypto import get_random_string<br>import datetime<br>from django.template.loader import render_to_string<br>from .forms import UserLoginViaOtpFormEmail<br>from django.contrib import messages<br>from django.db.models.functions import Now<br><br><br># Create your views here.<br><br>###############################<br>## LOGGING<br>import logging<br>logger_custom_string = logging.getLogger("custom_string")<br>from basic_django import settings<br>#usage:<br>#logger_custom_string.debug(settings.pp_odir(user_set))  # This will pretty print all the properties from dir(user_set)<br>#logger_custom_string.debug(settings.pp_dict(user_set.__dict__))  # This will pretty print any dictionary<br>#sql = str(user_set.query)<br>#sql = user_set.query.__str__()<br>#logger_custom_string.debug(settings.pp_sql_sql(sql)) # pretty print the sql obtained from the .query<br>#logger_custom_string.debug(settings.pp_sql_query_pg(user_set)) # pretty print the sql using mogrify only possible with Psycopg<br>#logger_custom_string.debug(settings.pp_sql_query_any(user_set)) # pretty print the sql using EXPLAIN. But runs extra sql<br>logger_database = logging.getLogger("django.db.backends")<br>#usage:<br>#logger_database.filters[0].open()<br>#logger_database.filters[0].close()<br><br>from .tasks import send_email_task<br><br>def user_login_via_otp_form_email(request):<br>    if request.method == 'POST':<br>        form = UserLoginViaOtpFormEmail(request.POST)<br>        if form.is_valid():<br>            email = form.cleaned_data.get('email')<br>            <br>            # Check to see if any users already exist with this email as a username.<br>            try:<br>                # GETTING THE USER based on email and creating a pin and saving the model.<br>                match = User.objects.get(email=email)<br>                # generate a random pin using crpto functions<br>                pin = get_random_string(length=6, allowed_chars='1234567890')<br>                match.otp_loginconfirm = pin<br>                # We have to use timezone datatime. So we use Now() which is used by Django in database<br>                match.otp_modified_date_loginconfirm = Now()<br>                match.save()<br>                <br>                # EMAIL subject and BODY<br>                # for BODY we use a template and render it with parameters<br>                subject = pin + ': To Login via OTP'<br>                # We to create the email body. So we create a template and pass the required arguments.<br>                # render_to_string will render the template with the context values<br>                message = render_to_string('login_register_password/login_via_otp/login_otp_sendemail.html', {<br>                    'user': match,<br>                    'pin': pin<br>                })<br><br>                # USING CELERY TASK for sending email Asynchronously<br>                #match.email_user(subject, message). This will delay the response <br>                # So will do this task asynchronously using celery<br>                # We have created a celery task. Using it we will send the email.<br>                # The code does not have to wait till the email is sent<br>                send_email_task.delay(match.email,subject,message)<br><br>                #USING MESSAGES to inform the user in the next page about email is being sent<br>                #we want to inform the user on the next page that email is being sent for OTP<br>                #For this we use messages<br>                messages.success(request, 'Email is being sent in TRY')<br><br>                # USING SESSION to make data available to next view.<br>                #For the next page we want to send some data which we dont want to display.<br>                request.session['email'] = email<br><br>                # REDIRECTING TO A DIFFERENT VIEW ie. different URL<br>                return redirect('login_register_password_namespace:user_login_via_otp_form_otp')<br>            except User.DoesNotExist:<br>                # SAME as above except here we create a new user<br>                newuser = form.save(commit=False)<br>                # generate a random pin<br>                pin = get_random_string(length=6, allowed_chars='1234567890')<br>                newuser.otp_loginconfirm = pin<br>                # We have to use timezone datatime. So we use Now() which is used by Django in database<br>                newuser.otp_modified_date_loginconfirm = Now()<br>                logger_custom_string.debug(settings.pp_odir(newuser))<br>                newuser.save()<br>                subject = pin + ': To Login via OTP'<br>                message = render_to_string('login_register_password/login_via_otp/login_otp_sendemail.html', {<br>                    'user': newuser,<br>                    'pin': pin<br>                })<br>                #newuser.email_user(subject, message)<br>                send_email_task.delay(newuser.email,subject,message)<br>                logger_custom_string.debug("task_activated")<br>                request.session['email'] = email<br>                messages.success(request, 'Email is being sent in EXCEPTION')<br>                return redirect('login_register_password_namespace:user_login_via_otp_form_otp')<br>    else:<br>        form = UserLoginViaOtpFormEmail(initial={'email': settings.TESTING_EMAIL})<br>        <br>    return render(request, 'login_register_password/login_via_otp/user_login_via_otp_form_email.html', {'form': form})<br><br>def user_login_via_otp_form_otp(request):<br>    return render(request, 'login_register_password/base.html')<br><br>    # if request.method == 'POST':<br>        # form = UserLoginViaOtpFormOTP(request.POST)<br>        # html = "&lt;html&gt;&lt;body&gt;OTP sent&lt;/body&gt;&lt;/html&gt;"<br>        # return HttpResponse(html)<br>    # else:<br>        # form = UserLoginViaOtpFormOTP(initial={'email': settings.TESTING_EMAIL})<br>    # return render(request, 'login_register_password/login_via_otp/user_login_via_otp_form_otp.html', {'form': form})<br><br></td></tr></tbody></table>

     * /home/web\_dev/django\_basic\_documentation/basic\_django/login\_register\_password/urls.py

     * Here we define urls to above two views and name them. And Also define app\_name

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>from django.urls import path<br>from . import views<br><br>app_name='login_register_password_app_name'<br><br>urlpatterns = [<br>    path('user_login_via_otp_form_email',views.user_login_via_otp_form_email, name='user_login_via_otp_form_email'),<br>    path('user_login_via_otp_form_otp',views.user_login_via_otp_form_otp, name='user_login_via_otp_form_otp'),<br>]<br></td></tr></tbody></table>

     * basic\_django/urls.py

     * Here we include all the urls from the app 'login\_register\_password and define namespace

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>"""basic_django URL Configuration<br><br>The `urlpatterns` list routes URLs to views. For more information please see:<br>    https://docs.djangoproject.com/en/2.2/topics/http/urls/<br>Examples:<br>Function views<br>    1. Add an import:  from my_app import views<br>    2. Add a URL to urlpatterns:  path('', views.home, name='home')<br>Class-based views<br>    1. Add an import:  from other_app.views import Home<br>    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')<br>Including another URLconf<br>    1. Import the include() function: from django.urls import include, path<br>    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))<br>"""<br>from django.contrib import admin<br>from django.urls import path<br>from . import views<br>from django.urls import path, include<br><br>urlpatterns = [<br>    path('admin/', admin.site.urls),<br>    path('login_register_password/', include('login_register_password.urls',namespace='login_register_password_namespace')),<br>    # this view is for testing 7commit related i.e sql logging, pretty printing, traceback <br>    path('test7commit',views.test_7commit, name='test_7commit'),<br>    # this view is for testing 8commit related i.e sending email by gmail smtp<br>    path('test8commit',views.test_8commit, name='test_8commit')<br><br>]<br><br></td></tr></tbody></table>

     * Tasks.py (See Celery and redis)

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>from basic_django import celery_app<br><br>from custom_user.models import User<br><br><br>###############################<br>## LOGGING<br>import logging<br>logger_custom_string = logging.getLogger("custom_string")<br>from basic_django import settings<br>#usage:<br>#logger_custom_string.debug("ANY STRING")<br>#logger_custom_string.debug(settings.pp_odir(user_set))  # This will pretty print all the properties from dir(user_set)<br>#logger_custom_string.debug(settings.pp_dict(user_set.__dict__))  # This will pretty print any dictionary<br>#sql = str(user_set.query)<br>#sql = user_set.query.__str__()<br>#logger_custom_string.debug(settings.pp_sql_sql(sql)) # pretty print the sql obtained from the .query<br>#logger_custom_string.debug(settings.pp_sql_query_pg(user_set)) # pretty print the sql using mogrify only possible with Psycopg<br>#logger_custom_string.debug(settings.pp_sql_query_any(user_set)) # pretty print the sql using EXPLAIN. But runs extra sql<br>logger_database = logging.getLogger("django.db.backends")<br>#usage:<br>#logger_database.filters[0].open()<br>#logger_database.filters[0].close()<br><br><br>#Note tasks can be declared anywhere. It has to lie in the INSTALLED APPS.<br>#os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'basic_django.settings') does the magic<br>#this will help celery to find all the tasks.<br><br><br>@celery_app.task<br>def send_email_task(email,subject,message):<br>    match = User.objects.get(email=email)<br>    match.email_user(subject,message)<br></td></tr></tbody></table>

* # TWELVETH COMMIT END

* # MISCELLENEOUS

 * ## Q: using model.save() from django shell will not validate the data

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>Creating an instance of a Model and calling save on that instance does not call full_clean. Therefore it’s possible for invalid data to enter your database if you don’t manually call the full_clean function before saving.<br><br>Object managers’ default create function also doesn’t call full_clean.<br><br>But in general, it's not good practice to add validation in the save() method. The reason is that in most Django apps, you'd create a form (a ModelForm) which would call the validation methods and be able to return something meaningful to the user when validation fails.<br><br>When the model's save() method is called it's too late to show something to the user, so you can only raise an exception at that point (and crash).<br><br>The normal procedure (which the admin forms use) is: validate the form by calling form.is_valid() (which calls full_clean() on the # model), then if and only if the form is valid, save the model.<br><br>The shell is not the regular interaction method and should be used only very carefully as it bypasses the normal flow of the application.<br></td></tr></tbody></table>

 * ## Tip: Log SQL Queries To Console

     * (from: https://avilpage.com/2018/05/django-tips-tricks-log-sql-queries-to-console.html)

     * Django ORM makes easy to interact with database. To understand what is happening behing the scenes or to see SQL performance, we can log all the SQL queries that be being executed. In this article, we will see various ways to achieve this.

     * ### Option 1: Django-debug-toolbar

       * Django debug toolbar provides panels to show debug information about requests. It has SQL panel which shows all executed SQL queries and time taken for them.

       * ![](images/image2.png)

       * #### \*\*\* Drawback: 

         * When building REST APIs or micro services where django templating engine is not used, this method won't work. In these situations, we have to log SQL queries to console.

     * ### Option 2: django-extensions

       * Django-extensions provides lot of utilities for productive development. For runserver\_plus and shell\_plus commands, it accepts and optional --print-sql argument, which prints all the SQL queries that are being executed.

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>./manage.py runserver_plus --print-sql<br>./manage.py shell_plus --print-sql<br></td></tr></tbody></table>

       * Whenever an SQL query gets executed, it prints the query and time taken for it in console.

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>In [42]: User.objects.filter(is_staff=True)<br>Out[42]: SELECT "auth_user"."id",<br>       "auth_user"."password",<br>       "auth_user"."last_login",<br>       "auth_user"."is_superuser",<br>       "auth_user"."username",<br>       "auth_user"."first_name",<br>       "auth_user"."last_name",<br>       "auth_user"."email",<br>       "auth_user"."is_staff",<br>       "auth_user"."is_active",<br>       "auth_user"."date_joined"<br>  FROM "auth_user"<br> WHERE "auth_user"."is_staff" = true<br> LIMIT 21<br><br><br>Execution time: 0.002107s [Database: default]<br><br>&lt;QuerySet [&lt;User: jjask&gt;, &lt;User: jhasdkj&gt;]&gt;<br></td></tr></tbody></table>

     * ### \*\*\* Print sql queries in jupyter notebook with django-extensions plugin

       * [https://stackoverflow.com/questions/51362648/print-sql-queries-in-jupyter-notebook-with-django-extensions-plugin](https://www.google.com/url?q=https://stackoverflow.com/questions/51362648/print-sql-queries-in-jupyter-notebook-with-django-extensions-plugin&sa=D&ust=1571383145082000)

       * [https://stackoverflow.com/a/54632855](https://www.google.com/url?q=https://stackoverflow.com/a/54632855&sa=D&ust=1571383145082000)

       * It's probably a bug in Django Extensions that you don't see SQL queries. A few versions ago, someone asked here how to disable SQL printing in Jupyter.

       * As a workaround, you could use django\_print\_sql:

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>from django_print_sql import print_sql<br>with print_sql(count_only=False):<br>    User.objects.count()<br></td></tr></tbody></table>

       * You may even find that having control over which queries to print is preferable to printing all.

       * But I mostly just print the last query retroactively:

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>from django import db<br>db.connection.queries[-1]<br></td></tr></tbody></table>

       * If you want to pretty-print the query with sqlparse, it starts getting complicated enough for a utility function:

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>import sqlparse<br>sqlparse.format(<br>    db.connection.queries[-1]['sql'], <br>    reindent=True, <br>    keyword_case='upper'<br>)<br></td></tr></tbody></table>

       * Check: Getting the sql of a query in jupyter also

     * ### Option 3: django-querycount

       * [https://github.com/bradmontgomery/django-querycount](https://www.google.com/url?q=https://github.com/bradmontgomery/django-querycount&sa=D&ust=1571383145088000)

       * Since Option2 does not show the number of queries, so we want to know more details of the of total number of queries, duplicate queries etc.

       * Django-querycount provides a middleware to show SQL query count and show duplicate queries on console.

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>pip install django-querycount<br><br>Just add querycount.middleware.QueryCountMiddleware to your MIDDLEWARE<br><br>Notice that django-querycount is hard coded to work only in DEBUG mode set to true<br><br>Settings:<br><br>QUERYCOUNT = {<br>    'THRESHOLDS': {<br>        'MEDIUM': 50,<br>        'HIGH': 200,<br>        'MIN_TIME_TO_LOG':0,<br>        'MIN_QUERY_COUNT_TO_LOG':0<br>    },<br>    'IGNORE_REQUEST_PATTERNS': [],<br>    'IGNORE_SQL_PATTERNS': [],<br>    'DISPLAY_DUPLICATES': None,<br>    'RESPONSE_HEADER': 'X-DjangoQueryCount-Count'<br>}<br><br><br>|------|-----------|----------|----------|----------|------------|<br>| Type | Database  |   Reads  |  Writes  |  Totals  | Duplicates |<br>|------|-----------|----------|----------|----------|------------|<br>| RESP |  default  |    3     |    0     |    3     |     1      |<br>|------|-----------|----------|----------|----------|------------|<br>Total queries: 3 in 1.7738s<br><br><br>Repeated 1 times.<br>SELECT "django_session"."session_key",<br>"django_session"."session_data", "django_session"."expire_date" FROM<br>"django_session" WHERE ("django_session"."session_key" =<br>'dummy_key AND "django_session"."expire_date"<br>&gt; '2018-05-31T09:38:56.369469+00:00'::timestamptz)<br></td></tr></tbody></table>

       * This package provides additional settings to customize output.

     * ### Option 4: Django logging

       * Instead of using any 3rd party package, we can use django.db.backends logger to print all the SQL queries.

       * (from: https://www.dabapps.com/blog/logging-sql-queries-django-13/)

       * To log all SQL queries, you'll need to add a few things to your LOGGING configuration dictionary in your settings.py. First, you'll need a handler. The example below logs everything at DEBUG level to the console (it'll appear in the output from Django's built-in development server).

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>LOGGING = {<br>    ...<br>    'handlers': {<br>        ...<br>        'console': {<br>            'level': 'DEBUG',<br>            'class': 'logging.StreamHandler',<br>        },<br>        ...<br>    },<br>    ...<br>}<br></td></tr></tbody></table>

       * Next, you'll need to add a logger that logs to this handler:

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td> 'loggers': {<br>        'django.db.backends': {<br>            'level': 'DEBUG',<br>            'handlers': ['console', ],<br>        },<br></td></tr></tbody></table>

       * Once the above is set up, you should see a stream of SQL queries in your runserver output. You might find, though, that this level of output is too verbose. It can be useful for debugging individual SQL queries, but it's a bit heavyweight for general use.

       * Combining above both setting.py (if LOGGING does not exist in the settings.py file at all)

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>LOGGING = {<br>    'version': 1,<br>    'disable_existing_loggers': False,<br>    'handlers': {<br>        'console': {<br>            'level': 'DEBUG',<br>            'class': 'logging.StreamHandler',<br>        },<br>    },<br>    'loggers': {<br>        'django.db.backends': {<br>            'level': 'DEBUG',<br>            'handlers': ['console', ],<br>        },<br>    },<br>}<br></td></tr></tbody></table>

       * #### Advantage: 

         * With this we can view SQL from "manage.py migrate", because I suspected it wasn't creating tables as I wanted. Your solution showed me those SQL queries and confirmed the tables weren't getting the "on delete cascade" set.

     * ### Option 4mod: Django logging when we want

       * Option 4: it will show sql queries for every server input/output

       * Instead we want to check for a particular view then

       * (from: https://stackoverflow.com/a/41389728/2897115)

       * And we can add this in our views.py

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>import logging<br><br>l = logging.getLogger('django.db.backends')<br>l.setLevel(logging.DEBUG)<br>l.addHandler(logging.StreamHandler())<br></td></tr></tbody></table>

     * ### Option 5: django-print-sql

       * [https://github.com/rabbit-aaron/django-print-sql](https://www.google.com/url?q=https://github.com/rabbit-aaron/django-print-sql&sa=D&ust=1571383145109000)

       * [https://stackoverflow.com/a/49318635/2897115](https://www.google.com/url?q=https://stackoverflow.com/a/49318635/2897115&sa=D&ust=1571383145110000)

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>$ pipenv install django-print-sql<br>$ pipenv install sqlparse (If sqlparse is installed, the SQL statement wil be formatted.)<br><br>from django_print_sql import print_sql_decorator<br><br>@print_sql_decorator(count_only=False)  # this works on class-based views as well<br>def get(request):<br>    # your view code here<br></td></tr></tbody></table>

     * ### Option 6: sql log

       * https://stackoverflow.com/a/23975393/2897115

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>sudo su postgres<br>tail -f /var/log/postgresql/postgresql-8.4-main.log<br><br>don't forget to set log_statement='all' in postgresql.conf for this method<br></td></tr></tbody></table>

 * ## Understanding logging in Python:

     * [https://fangpenlin.com/posts/2012/08/26/good-logging-practice-in-python/](https://www.google.com/url?q=https://fangpenlin.com/posts/2012/08/26/good-logging-practice-in-python/&sa=D&ust=1571383145115000)

     * ### print is not a good idea

       * Although logging is important, not all developers know how to use them correctly. I saw some developers insert print statements when developing and remove those statements when it is finished. It may looks like this

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>print 'Start reading database'<br>records = model.read_recrods()<br>print '# records', records<br>print 'Updating record ...'<br>model.update_records(records)<br>print 'done'<br></td></tr></tbody></table>

       * Cons:

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>&gt;It works when the program is a simple script, but for complex systems, you better not to use this approach.<br>&gt;you may forgot to remove those unused prints<br>&gt;You also cannot control those print statements without modifying code<br>&gt;And all printed messages go into stdout, which is bad when you have data to output to stdout.<br></td></tr></tbody></table>

     * ### 

     * ### Use Python standard logging module

       * Example using logging 

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>import logging<br>logger = logging.getLogger(__name__)<br>logger.setLevel(logging.INFO)<br>logger.info('Start reading database')<br># read database here<br>records = {'john': 55, 'tom': 66}<br>logger.debug('Records: %s', records)<br>logger.info('Updating records ...')<br># update records here<br>logger.info('Finish updating records')<br></td></tr></tbody></table>

       * You can run it and see

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>INFO:__main__:Start reading database<br>INFO:__main__:Updating records ...<br>INFO:__main__:Finish updating records<br></td></tr></tbody></table>

       * Let’s change the logger level to DEBUG and see the output again

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>#gauranga<br>logger.setLevel(logging.INFO)<br></td></tr></tbody></table>

       * The output:

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>INFO:__main__:Start reading database<br>DEBUG:__main__:Records: {'john': 55, 'tom': 66}<br>INFO:__main__:Updating records ...<br>INFO:__main__:Finish updating records<br></td></tr></tbody></table>

       * As you can see, we adjust the logger level to DEBUG, then debug records appear in output. 

       * You can also decide how these messages are processed. For example, you can use a FileHandler to write records to a file.

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>import logging<br><br>logger = logging.getLogger(__name__)<br>logger.setLevel(logging.INFO)<br><br># create a file handler<br>handler = logging.FileHandler('hello.log')<br>handler.setLevel(logging.INFO)<br><br># create a logging format<br>formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')<br>handler.setFormatter(formatter)<br><br># add the handlers to the logger<br>logger.addHandler(handler)<br><br>logger.info('Hello baby')<br></td></tr></tbody></table>

       * There are different handlers, you can also send records to you mailbox or even a to a remote server.

       * https://www.toptal.com/python/in-depth-python-logging

     * ### PYTHON LOGGING LEVELS

       * The log level corresponds to the “importance” a log is given: an “error” log should be more urgent then than the “warn” log, whereas a “debug” log should be useful only when debugging the application.

       * https://fangpenlin.com/posts/2012/08/26/good-logging-practice-in-python/

       * By giving different level to logger or handler, you can write only error messages to specific log file, or record debug details when debugging. 

       * https://www.toptal.com/python/in-depth-python-logging

       * There are six log levels in Python; each level is associated with an integer that indicates the log severity: NOTSET=0, DEBUG=10, INFO=20, WARN=30, ERROR=40, and CRITICAL=50.

       * https://mussol.org/2016/12/15/understanding-logging-in-python/

       * So a logger configured in level WARNING (the default with the RootLogger) will process log records tagged WARNING, ERROR and CRITICAL. But not DEBUG or INFO.

       * https://mussol.org/2016/12/15/understanding-logging-in-python/

     * ### There are 4 main concepts in Python logging:

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>&gt; Loggers : expose the interface that application code directly uses<br>&gt; Handlers : send the log records (created by loggers) to the appropriate destination<br>&gt; Filters : provide a finer grained facility for determining which log records to output<br>&gt; Formatters : specify the layout of log records in the final output<br></td></tr></tbody></table>

       * You can add from zero to several handlers to the same logger. 

       * In the same way, you can apply from zero to several filters to handlers or loggers.

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>First important thing you need to know is that the logging module in Python is implemented as a hierarchy of loggers, being the RootLogger the main one. Being so, any logger you create will be a descendent of the RootLogger. Thus all the handlers and filters applied to the RootLogger will be applied to the rest of the loggers. It is very important to have this in mind while configuring your logging strategy. For example, you probably don’t want to add a FileHandler to the RootLogger, since that will make all the log records from your code and the libraries you use to be stored in a file.<br><br>The second important concept is that you can create descendants of a logger this way:<br><br>import logging<br><br>parent_log = logging.getLogger('parent')<br>child_1 = logging.getLogger('parent.child_1')<br>child_2 = logging.getLogger('parent.child_2')<br><br>child_1 and child_2 will now inherit handlers, formatters and filters from parent_log (as well as from RootLogger).<br></td></tr></tbody></table>

       * https://mussol.org/2016/12/15/understanding-logging-in-python/

     * ### Example - Configuring logging

       * There are mainly two ways of configuring logging: via code or via configuration files.

       * I personally think its always better to separate the configuration from the code, so let’s write a configuration file.

       * We want to log everything on the console, but only those records from our app to a file for longer term storage. To do so, we will attach a StreamHandler to the RootLogger. This will “swallow” all the records and spit them in the console. 

       * To save the records from our app (called myapp) we will attach a RotatingFileHandler to the main logger of our app. We only need to add it to the parent logger, since all descendants will inherit it.

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>version: 1<br><br>formatters:<br>    custom_format:<br>        format: "%(asctime)s - %(name)s - %(levelname)s - %(message)s"<br><br>filters:<br>    myapp:<br>        name: myapp<br><br>handlers:<br>    console:<br>        class: logging.StreamHandler<br>        formatter: custom_format<br>    file:<br>        class: logging.handlers.RotatingFileHandler<br>        formatter: custom_format<br>        filename: myapp.log<br>        filters: [myapp]<br>        maxBytes: 1024<br>        backupCount: 5<br><br>loggers:<br>    '':<br>        handlers: [console]<br>        level: INFO<br>    myapp:<br>        handlers: [file]<br>        level: INFO<br></td></tr></tbody></table>

       * NOTE: '' its a special name to modify the RootLogger

       * Hopefully the configuration file is quite self-explanatory once you know the parameters each handler requires. Now you only need to load the configuration and start logging:

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>import yaml<br>import logging<br>import logging.config<br><br>with open('config.yaml', 'r') as f:<br>    conf = yaml.load(f)<br><br>logging.config.dictConfig(conf)<br><br>myapp = logging.getLogger('myapp')<br>myapp.info('This logger will write both to console and to the logging file, since the logger\'s name is myapp')<br><br>myapp_api = logging.getLogger('myapp.api')<br>myapp_api.info('This should also write to both since its a descendant of myapp')<br><br>another_logger = logging.getLogger('another_app')<br>another_logger.info('This instead should only appear in the console')<br></td></tr></tbody></table>

       * If you run that code, this will be the output in the console:

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>2016-12-15 10:57:05,344 - myapp - INFO - This logger will write both to console and to the logging file, since the logger's name is myapp<br>2016-12-15 10:57:05,345 - myapp - INFO - This should also write to both since its a descendant of myapp<br>2016-12-15 10:57:05,345 - another_app - INFO - This instead should only appear in the console<br></td></tr></tbody></table>

       * And this will be the content of the file myapp.log:

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>2016-12-15 10:58:13,631 - myapp - INFO - This logger will write both to console and to the logging file, since the logger's name is myapp<br>2016-12-15 10:58:13,631 - myapp.api - INFO - This should also write to both since its a descendant of myapp<br></td></tr></tbody></table>

       * https://www.toptal.com/python/in-depth-python-logging

     * ### PYTHON LOGGING HANDLER

       * The log handler is the component that effectively writes/displays a log: 

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>&gt; Display it in the console (via StreamHandler), <br>Eg: console_handler = logging.StreamHandler()<br>&gt; in a file (via FileHandler), <br>Eg: file_handler = logging.FileHandler("filename")<br>&gt; or even by sending you an email via SMTPHandler, etc.<br></td></tr></tbody></table>

       * Each log handler has 2 important fields:

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>&gt; A formatter which adds context information to a log.<br>&gt; A log level that filters out logs whose levels are inferior. So a log handler with the INFO level will not handle DEBUG logs.<br>So a logger configured in level WARNING (the default with the RootLogger) will process log records tagged WARNING, ERROR and CRITICAL. But not DEBUG or INFO.<br></td></tr></tbody></table>

       * Handlers are propagated like levels. If the logger has no handler set, its chain of ancestors is search for a handler.

     * ### PYTHON LOGGER

       * Logger is probably the one that will be used directly the most often in the code and which is also the most complicated. A new logger can be obtained by:

       * toto\_logger = logging.getLogger("toto")

     * ### A logger has three main fields:

       * Propagate: Decides whether a log should be propagated to the logger’s parent. By default, its value is True.

       * A level: Like the log handler level, the logger level is used to filter out “less important” logs. Except, unlike the log handler, the level is only checked at the “child” logger; once the log is propagated to its parents, the level will not be checked. This is rather an un-intuitive behavior.

       * Handlers: The list of handlers that a log will be sent to when it arrives to a logger. This allows a flexible log handling—for example, you can have a file log handler that logs all DEBUG logs and an email log handler that will only be used for CRITICAL logs. In this regard, the logger-handler relationship is similar to a publisher-consumer one: A log will be broadcast to all handlers once it passes the logger level check.

     * ### A logger is unique by name,

       * A logger is unique by name, meaning that if a logger with the name “toto” has been created, the consequent calls of logging.getLogger("toto") will return the same object:

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>#gauranga<br>assert id(logging.getLogger("toto")) == id(logging.getLogger("toto"))<br></td></tr></tbody></table>

     * ### Root logger

       * As you might have guessed, loggers have a hierarchy. On top of the hierarchy is the root logger, which can be accessed via logging.root. This logger is called when methods like logging.debug() is used. By default, the root log level is WARN, so every log with lower level (for example via logging.info("info")) will be ignored. Another particularity of the root logger is that its default handler will be created the first time a log with a level greater than WARN is logged. Using the root logger directly or indirectly via methods like logging.debug() is generally not recommended.

       * http://zetcode.com/python/logging/

       * All loggers are descendants of the root logger. Each logger passes log messages on to its parent. New loggers are created with the getLogger(name) method. Calling the function without a name (getLogger()) returns the root logger.

       * The root logger always has an explicit level set, which is WARNING by default.

       * The root looger sits at the top of the hierarchy and is always present, even if not configured. In general, the program or library should not log directly against the root logger. Instead a specific logger for the program should be configured. Root logger can be used to easily turn all loggers from all libraries on and off.

       * Python logging simple example:

       * The logging module has simple methods that can be used right away without any cofiguration. This can be used for simple logging.

       * simple.py

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>#!/usr/bin/env python<br><br>import logging<br><br>logging.debug('This is a debug message')<br>logging.info('This is an info message')<br>logging.warning('This is a warning message')<br>logging.error('This is an error message')<br>logging.critical('This is a critical message')<br></td></tr></tbody></table>

       * The example calls five methods of the logging module. The messages are written to the console.

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>$ simple.py<br>WARNING:root:This is a warning message<br>ERROR:root:This is an error message<br>CRITICAL:root:This is a critical message<br></td></tr></tbody></table>

       * Notice that root logger is used and only three messages were written. This is because by default, only messages with level warning and up are written.

     * ### Parent logger (a.b)

       * By default, when a new logger is created, its parent will be set to the root logger:

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>lab = logging.getLogger("a.b")<br>assert lab.parent == logging.root # lab's parent is indeed the root logger<br></td></tr></tbody></table>

       * However, the logger uses the “dot notation,” meaning that a logger with the name “a.b” will be the child of the logger “a.” However, this is only true if the logger “a” has been created, otherwise “a.b” parent is still the root.

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>la = logging.getLogger("a")<br>assert lab.parent == la # lab's parent is now la instead of root<br></td></tr></tbody></table>

       * https://www.electricmonk.nl/log/2017/08/06/understanding-pythons-logging-module/

     * ### Logger hierarchy

       * Loggers have a hierarchy. That is, you can create individual loggers and each logger has a parent. At the top of the hierarchy is the root logger. For instance, we could have the following loggers:

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>myapp<br>myapp.ui<br>myapp.ui.edit<br></td></tr></tbody></table>

       * These can be created by asking a parent logger for a new child logger:

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>&gt;&gt;&gt; log_myapp = logging.getLogger("myapp")<br>&gt;&gt;&gt; log_myapp_ui = log_myapp.getChild("ui")<br>&gt;&gt;&gt; log_myapp_ui.name<br>'myapp.ui'<br>&gt;&gt;&gt; log_myapp_ui.parent.name<br>'myapp'<br></td></tr></tbody></table>

       * Or you can use dot notation:

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>&gt;&gt;&gt; log_myapp_ui = logging.getLogger("myapp.ui")<br>&gt;&gt;&gt; log_myapp_ui.parent.name<br>'myapp'<br></td></tr></tbody></table>

       * You should use the dot notation generally.

       * One thing that’s not immediately clear is that the logger names don’t include the root logger. In actuality, the logger hierarchy looks like this:

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>root.myapp<br>root.myapp.ui<br>root.myapp.ui.edit<br></td></tr></tbody></table>

       * More on the root logger in a bit.

       * https://www.toptal.com/python/in-depth-python-logging

     * ### Effective logger level w.r.t NOTSET and w.r.t parent is root or not

       * When a logger decides whether a log should pass according to the level check (e.g., if the log level is lower than logger level, the log will be ignored), it uses its “effective level” instead of the actual level. 

       * The effective level is the same as logger level if the level is not NOTSET, i.e., all the values from DEBUG up to CRITICAL; 

       * however, if the logger level is NOTSET, then the effective level will be the first ancestor level that has a non-NOTSET level.

       * Python effective logging level

       * The effective logging level is the level set explicitly or determined from the logger parents.

       * effective\_level.py

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>#!/usr/bin/env python<br><br>import logging<br><br>main_logger = logging.getLogger('main')<br>main_logger.setLevel(5)<br><br>dev_logger = logging.getLogger('main.dev')<br><br>print(main_logger.getEffectiveLevel())<br>print(dev_logger.getEffectiveLevel())<br></td></tr></tbody></table>

       * In the example, we examine the effective logging level of two loggers.

       * The level of the dev\_logger is not set; the level of its parent is then used.

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>$ effective_level.py<br>5<br>5<br></td></tr></tbody></table>

       * This is the output.

     * ### NOTSET level and Log Level vs logger level

       * By default, a new logger has the NOTSET level, and as the root logger has a WARN level, the logger’s effective level will be WARN. So even if a new logger has some handlers attached, these handlers will not be called unless the log level exceeds WARN:

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>toto_logger = logging.getLogger("toto")<br>assert toto_logger.level == logging.NOTSET # new logger has NOTSET level<br>assert toto_logger.getEffectiveLevel() == logging.WARN # and its effective level is the root logger level, i.e. WARN<br><br># attach a console handler to toto_logger<br>console_handler = logging.StreamHandler()<br>toto_logger.addHandler(console_handler)<br>toto_logger.debug("debug") # nothing is displayed as the log level DEBUG is smaller than toto effective level<br>toto_logger.setLevel(logging.DEBUG)<br>toto_logger.debug("debug message") # now you should see "debug message" on screen<br></td></tr></tbody></table>

       * By default, the logger level will be used to decide of the a log passes: If the log level is lower than logger level, the log will be ignored.

       * Note: logger level is toto\_logger.setLevel(logging.DEBUG) where as log level is toto\_logger.debug or toto\_logger.info

     * ### use \_\_name\_\_ as the logger name: 

       * log = logging.getLogger(\_\_name\_\_). This uses the module hierarchy as the name, which is generally what you want. 

       * ===========================

 * ## How to show queries log in PostgreSQL?

     * ===========================

     * [https://tableplus.io/blog/2018/10/how-to-show-queries-log-in-postgresql.html](https://www.google.com/url?q=https://tableplus.io/blog/2018/10/how-to-show-queries-log-in-postgresql.html&sa=D&ust=1571383145187000)

     * Please note that only those queries that are executed can be logged.

     * In the config file at /var/lib/postgres/data/postgresql.conf change the following

     * Before changing take a backup of postgresql.config fiile

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>log_statement = 'all'<br>log_directory = 'pg_log'<br>log_filename = 'postgresql-%Y-%m-%d_%H%M%S.log'<br>logging_collector = on<br>log_min_error_statement = error<br></td></tr></tbody></table>

     * Then restart

     * sudo service postgresql restart

     * ===========================

 * ## Django: Database access optimization:

     * https://docs.djangoproject.com/en/2.2/topics/db/optimization/

     * ===========================

     * Understand QuerySets¶

     * Understanding QuerySets is vital to getting good performance with simple code. In particular:

     * Understand QuerySet evaluation¶

     * To avoid performance problems, it is important to understand:

     * \> that QuerySets are lazy.

     * \> when they are evaluated.

     * \> how the data is held in memory.

     * ===========================

 * ## QuerySets are lazy

     * https://docs.djangoproject.com/en/2.2/topics/db/queries/\#querysets-are-lazy

     * ===========================

     * QuerySets are lazy – the act of creating a QuerySet doesn’t involve any database activity. You can stack filters together all day long, and Django won’t actually run the query until the QuerySet is evaluated. Take a look at this example:

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>&gt;&gt;&gt; q = Entry.objects.filter(headline__startswith="What")<br>&gt;&gt;&gt; q = q.filter(pub_date__lte=datetime.date.today())<br>&gt;&gt;&gt; q = q.exclude(body_text__icontains="food")<br>&gt;&gt;&gt; print(q)<br></td></tr></tbody></table>

     * Though this looks like three database hits, in fact it hits the database only once, at the last line (print(q)). In general, the results of a QuerySet aren’t fetched from the database until you “ask” for them. When you do, the QuerySet is evaluated by accessing the database. For more details on exactly when evaluation takes place, see When QuerySets are evaluated.

     * ===========================

 * ## When QuerySets are evaluated

     * https://docs.djangoproject.com/en/2.2/ref/models/querysets/\#when-querysets-are-evaluated

     * ===========================

     * Internally, a QuerySet can be constructed, filtered, sliced, and generally passed around without actually hitting the database. No database activity actually occurs until you do something to evaluate the queryset.

     * You can evaluate a QuerySet in the following ways:

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>&gt;&gt; Iteration. A QuerySet is iterable, and it executes its database query the first time you iterate over it. For example, this will print the headline of all entries in the database:<br><br>for e in Entry.objects.all():<br>    print(e.headline)<br>Note: Don’t use this if all you want to do is determine if at least one result exists. It’s more efficient to use exists().<br><br>&gt;&gt; Slicing. As explained in Limiting QuerySets, a QuerySet can be sliced, using Python’s array-slicing syntax. Slicing an unevaluated QuerySet usually returns another unevaluated QuerySet, but Django will execute the database query if you use the “step” parameter of slice syntax, and will return a list. Slicing a QuerySet that has been evaluated also returns a list.<br><br>Also note that even though slicing an unevaluated QuerySet returns another unevaluated QuerySet, modifying it further (e.g., adding more filters, or modifying ordering) is not allowed, since that does not translate well into SQL and it would not have a clear meaning either.<br><br>&gt;&gt; Pickling/Caching. See the following section for details of what is involved when pickling QuerySets. The important thing for the purposes of this section is that the results are read from the database.<br><br>&gt;&gt; repr(). A QuerySet is evaluated when you call repr() on it. This is for convenience in the Python interactive interpreter, so you can immediately see your results when using the API interactively.<br><br>&gt;&gt; len(). A QuerySet is evaluated when you call len() on it. This, as you might expect, returns the length of the result list.<br><br>&gt;&gt; Note: If you only need to determine the number of records in the set (and don’t need the actual objects), it’s much more efficient to handle a count at the database level using SQL’s SELECT COUNT(*). Django provides a count() method for precisely this reason.<br><br>&gt;&gt; list(). Force evaluation of a QuerySet by calling list() on it. For example:<br><br>entry_list = list(Entry.objects.all())<br><br>&gt;&gt; bool(). Testing a QuerySet in a boolean context, such as using bool(), or, and or an if statement, will cause the query to be executed. If there is at least one result, the QuerySet is True, otherwise False. For example:<br><br>if Entry.objects.filter(headline="Test"):<br>   print("There is at least one Entry with the headline Test")<br><br>&gt;&gt; Note: If you only want to determine if at least one result exists (and don’t need the actual objects), it’s more efficient to use exists().<br></td></tr></tbody></table>

 * ## Logging and propogate:

     * Why to use propogate=False when root handler is mentioned

     * In this Logging we used propogate=False for django.db.backends

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>LOGGING = {<br>    'version': 1,<br>    'disable_existing_loggers': False,<br>    'formatters': {<br>        'sql': {<br>            '()': SQLFormatter,<br>            'format': '[%(duration).3f] %(statement)s',<br>        },<br>        'verbose': {<br>            'format': '%(levelname)s %(funcName)s() %(pathname)s[:%(lineno)s] %(name)s \n%(message)s'<br>        }<br>    },<br>    'handlers': {<br>        'console': {<br>            'level': 'DEBUG',<br>            'formatter': 'verbose',<br>            'class': 'logging.StreamHandler',<br>        },<br>        'sql': {<br>            'class': 'logging.StreamHandler',<br>            'formatter': 'sql',<br>            'level': 'DEBUG',<br>        },<br>    },<br>    'loggers': {<br>        'django.db.backends': {<br>            'handlers': ['sql'],<br>            'level': 'DEBUG',<br>            'propagate': False,<br>        },<br>        '': {<br>            'level': 'DEBUG' if DEBUG else 'INFO',<br>            'handlers': ['console']<br>        }<br>    }<br>}<br></td></tr></tbody></table>

     * The reason root logging handler here.

     * First we try with without root handler and not mention about propogate. By default propogate= true

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>LOGGING = {<br>    'version': 1,<br>    'disable_existing_loggers': False,<br>    'formatters': {<br>        'sql': {<br>            '()': SQLFormatter,<br>            'format': '[%(duration).3f] %(statement)s',<br>        },<br>        'verbose': {<br>            'format': '%(levelname)s %(funcName)s() %(pathname)s[:%(lineno)s] %(name)s \n%(message)s'<br>        }<br>    },<br>    'handlers': {<br>        'console': {<br>            'level': 'DEBUG',<br>            'formatter': 'verbose',<br>            'class': 'logging.StreamHandler',<br>        },<br>        'sql': {<br>            'class': 'logging.StreamHandler',<br>            'formatter': 'sql',<br>            'level': 'DEBUG',<br>        }<br>    },<br>    'loggers': {<br>        'django.db.backends': {<br>            'handlers': ['sql'],<br>            'level': 'DEBUG',<br>        },<br>        'django.db.backends.schema': {<br>            'handlers': ['console'],<br>            'level': 'DEBUG',<br>        },<br>    }<br>}<br></td></tr></tbody></table>

     * The view function is:

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>def test1(request):<br><br>    user_set = User.objects.all()<br>    print(user_set)<br><br>    now = datetime.datetime.now()<br>    html = "&lt;html&gt;&lt;body&gt;It is now %s.&lt;/body&gt;&lt;/html&gt;" % now<br>    return HttpResponse(html)<br></td></tr></tbody></table>

     * The output is

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>[0.001] SELECT "custom_user_user"."id",<br>       "custom_user_user"."password",<br>       "custom_user_user"."last_login",<br>       "custom_user_user"."is_superuser",<br>       "custom_user_user"."is_staff",<br>       "custom_user_user"."date_joined",<br>       "custom_user_user"."first_name",<br>       "custom_user_user"."last_name",<br>       "custom_user_user"."email",<br>       "custom_user_user"."is_active",<br>       "custom_user_user"."about",<br>       "custom_user_user"."location",<br>       "custom_user_user"."birth_date",<br>       "custom_user_user"."email_confirmed",<br>       "custom_user_user"."jwt_secret",<br>       "custom_user_user"."otp_emailconfirm",<br>       "custom_user_user"."otp_passconfirm",<br>       "custom_user_user"."otp_loginconfirm",<br>       "custom_user_user"."otp_modified_date_emailconfirm",<br>       "custom_user_user"."otp_modified_date_passconfirm",<br>       "custom_user_user"."otp_modified_date_loginconfirm",<br>       "custom_user_user"."modified_date"<br>FROM "custom_user_user"<br>LIMIT 21<br><br>&lt;QuerySet [&lt;User: admin@admin.com&gt;]&gt;<br>[12/Aug/2019 10:39:53] "GET /test1 HTTP/1.1" 200 63<br></td></tr></tbody></table>

     * Whereas if i define root handler (we use root handler for having logger = logging.getLogger(\_\_name\_\_)) then the sql is printed twice

     * The logging config

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>LOGGING = {<br>    'version': 1,<br>    'disable_existing_loggers': False,<br>    'formatters': {<br>        'sql': {<br>            '()': SQLFormatter,<br>            'format': '[%(duration).3f] %(statement)s',<br>        },<br>        'verbose': {<br>            'format': '%(levelname)s %(funcName)s() %(pathname)s[:%(lineno)s] %(name)s \n%(message)s'<br>        }<br>    },<br>    'handlers': {<br>        'console': {<br>            'level': 'DEBUG',<br>            'formatter': 'verbose',<br>            'class': 'logging.StreamHandler',<br>        },<br>        'sql': {<br>            'class': 'logging.StreamHandler',<br>            'formatter': 'sql',<br>            'level': 'DEBUG',<br>        }<br>    },<br>    'loggers': {<br>        'django.db.backends': {<br>            'handlers': ['sql'],<br>            'level': 'DEBUG',<br>        },<br>        'django.db.backends.schema': {<br>            'handlers': ['console'],<br>            'level': 'DEBUG',<br>        },<br>        '': {<br>            'level': 'DEBUG' if DEBUG else 'INFO',<br>            'handlers': ['console']<br>        }<br>    }<br>}<br></td></tr></tbody></table>

     * The output is

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>[0.001] SELECT "custom_user_user"."id",<br>       "custom_user_user"."password",<br>       "custom_user_user"."last_login",<br>       "custom_user_user"."is_superuser",<br>       "custom_user_user"."is_staff",<br>       "custom_user_user"."date_joined",<br>       "custom_user_user"."first_name",<br>       "custom_user_user"."last_name",<br>       "custom_user_user"."email",<br>       "custom_user_user"."is_active",<br>       "custom_user_user"."about",<br>       "custom_user_user"."location",<br>       "custom_user_user"."birth_date",<br>       "custom_user_user"."email_confirmed",<br>       "custom_user_user"."jwt_secret",<br>       "custom_user_user"."otp_emailconfirm",<br>       "custom_user_user"."otp_passconfirm",<br>       "custom_user_user"."otp_loginconfirm",<br>       "custom_user_user"."otp_modified_date_emailconfirm",<br>       "custom_user_user"."otp_modified_date_passconfirm",<br>       "custom_user_user"."otp_modified_date_loginconfirm",<br>       "custom_user_user"."modified_date"<br>FROM "custom_user_user"<br>LIMIT 21<br><br>DEBUG execute() /home/web_dev/django_basic_documentation/.venv/lib/python3.7/site-packages/django/db/backends/utils.py[:110] django.db.backends <br>(0.001) SELECT "custom_user_user"."id", "custom_user_user"."password", "custom_user_user"."last_login", "custom_user_user"."is_superuser", "custom_user_user"."is_staff", "custom_user_user"."date_joined", "custom_user_user"."first_name", "custom_user_user"."last_name", "custom_user_user"."email", "custom_user_user"."is_active", "custom_user_user"."about", "custom_user_user"."location", "custom_user_user"."birth_date", "custom_user_user"."email_confirmed", "custom_user_user"."jwt_secret", "custom_user_user"."otp_emailconfirm", "custom_user_user"."otp_passconfirm", "custom_user_user"."otp_loginconfirm", "custom_user_user"."otp_modified_date_emailconfirm", "custom_user_user"."otp_modified_date_passconfirm", "custom_user_user"."otp_modified_date_loginconfirm", "custom_user_user"."modified_date" FROM "custom_user_user"  LIMIT 21; args=()<br>&lt;QuerySet [&lt;User: admin@admin.com&gt;]&gt;<br>[12/Aug/2019 10:47:23] "GET /test1 HTTP/1.1" 200 63<br></td></tr></tbody></table>

     * Here we can see that the sql is shown twice in the console.

     * To avoid that we use propogate=False

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>LOGGING = {<br>    'version': 1,<br>    'disable_existing_loggers': False,<br>    'formatters': {<br>        'sql': {<br>            '()': SQLFormatter,<br>            'format': '[%(duration).3f] %(statement)s',<br>        },<br>        'verbose': {<br>            'format': '%(levelname)s %(funcName)s() %(pathname)s[:%(lineno)s] %(name)s \n%(message)s'<br>        }<br>    },<br>    'handlers': {<br>        'console': {<br>            'level': 'DEBUG',<br>            'formatter': 'verbose',<br>            'class': 'logging.StreamHandler',<br>        },<br>        'sql': {<br>            'class': 'logging.StreamHandler',<br>            'formatter': 'sql',<br>            'level': 'DEBUG',<br>        }<br>    },<br>    'loggers': {<br>        'django.db.backends': {<br>            'handlers': ['sql'],<br>            'level': 'DEBUG',<br>            'propagate': False,<br>        },<br>        'django.db.backends.schema': {<br>            'handlers': ['console'],<br>            'level': 'DEBUG',<br>            'propagate': False,<br>        },<br>        '': {<br>            'level': 'DEBUG' if DEBUG else 'INFO',<br>            'handlers': ['console']<br>        }<br>    }<br>}<br></td></tr></tbody></table>

     * The output is

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>[0.001] SELECT "custom_user_user"."id",<br>       "custom_user_user"."password",<br>       "custom_user_user"."last_login",<br>       "custom_user_user"."is_superuser",<br>       "custom_user_user"."is_staff",<br>       "custom_user_user"."date_joined",<br>       "custom_user_user"."first_name",<br>       "custom_user_user"."last_name",<br>       "custom_user_user"."email",<br>       "custom_user_user"."is_active",<br>       "custom_user_user"."about",<br>       "custom_user_user"."location",<br>       "custom_user_user"."birth_date",<br>       "custom_user_user"."email_confirmed",<br>       "custom_user_user"."jwt_secret",<br>       "custom_user_user"."otp_emailconfirm",<br>       "custom_user_user"."otp_passconfirm",<br>       "custom_user_user"."otp_loginconfirm",<br>       "custom_user_user"."otp_modified_date_emailconfirm",<br>       "custom_user_user"."otp_modified_date_passconfirm",<br>       "custom_user_user"."otp_modified_date_loginconfirm",<br>       "custom_user_user"."modified_date"<br>FROM "custom_user_user"<br>LIMIT 21<br><br>&lt;QuerySet [&lt;User: admin@admin.com&gt;]&gt;<br>[12/Aug/2019 10:49:14] "GET /test1 HTTP/1.1" 200 63<br></td></tr></tbody></table>

     * So here we are using root logging handler and also able to not repeat the sql again by using progogate = false

 * ## Logging and query sets are Lazy:

     * With the below  Logging config

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>LOGGING = {<br>    'version': 1,<br>    'disable_existing_loggers': False,<br>    'formatters': {<br>        'sql': {<br>            '()': SQLFormatter,<br>            'format': '[%(duration).3f] %(statement)s',<br>        },<br>        'verbose': {<br>            'format': '%(levelname)s %(funcName)s() %(pathname)s[:%(lineno)s] %(name)s \n%(message)s'<br>        }<br>    },<br>    'handlers': {<br>        'console': {<br>            'level': 'DEBUG',<br>            'formatter': 'verbose',<br>            'class': 'logging.StreamHandler',<br>        },<br>        'sql': {<br>            'class': 'logging.StreamHandler',<br>            'formatter': 'sql',<br>            'level': 'DEBUG',<br>        }<br>    },<br>    'loggers': {<br>        'django.db.backends': {<br>            'handlers': ['sql'],<br>            'level': 'DEBUG',<br>            'propagate': False,<br>        },<br>        'django.db.backends.schema': {<br>            'handlers': ['console'],<br>            'level': 'DEBUG',<br>            'propagate': False,<br>        },<br>        '': {<br>            'level': 'DEBUG' if DEBUG else 'INFO',<br>            'handlers': ['console']<br>        }<br>    }<br>}<br></td></tr></tbody></table>

     * If we have the following view function in the views.py. It will not show any sql in logging

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>def test1(request):<br><br>    user_set = User.objects.all()<br><br>    now = datetime.datetime.now()<br>    html = "&lt;html&gt;&lt;body&gt;It is now %s.&lt;/body&gt;&lt;/html&gt;" % now<br>    return HttpResponse(html)<br></td></tr></tbody></table>

     * Where as if we try to print(user\_set) then it will show sql in console.

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>def test1(request):<br><br>    user_set = User.objects.all()<br>    print(user_set)<br><br>    now = datetime.datetime.now()<br>    html = "&lt;html&gt;&lt;body&gt;It is now %s.&lt;/body&gt;&lt;/html&gt;" % now<br>    return HttpResponse(html)<br></td></tr></tbody></table>

     * The output is:

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>[0.001] SELECT "custom_user_user"."id",<br>       "custom_user_user"."password",<br>       "custom_user_user"."last_login",<br>       "custom_user_user"."is_superuser",<br>       "custom_user_user"."is_staff",<br>       "custom_user_user"."date_joined",<br>       "custom_user_user"."first_name",<br>       "custom_user_user"."last_name",<br>       "custom_user_user"."email",<br>       "custom_user_user"."is_active",<br>       "custom_user_user"."about",<br>       "custom_user_user"."location",<br>       "custom_user_user"."birth_date",<br>       "custom_user_user"."email_confirmed",<br>       "custom_user_user"."jwt_secret",<br>       "custom_user_user"."otp_emailconfirm",<br>       "custom_user_user"."otp_passconfirm",<br>       "custom_user_user"."otp_loginconfirm",<br>       "custom_user_user"."otp_modified_date_emailconfirm",<br>       "custom_user_user"."otp_modified_date_passconfirm",<br>       "custom_user_user"."otp_modified_date_loginconfirm",<br>       "custom_user_user"."modified_date"<br>FROM "custom_user_user"<br>LIMIT 21<br><br>&lt;QuerySet [&lt;User: admin@admin.com&gt;]&gt;<br>[12/Aug/2019 10:49:14] "GET /test1 HTTP/1.1" 200 63<br></td></tr></tbody></table>

 * ## Logging and jupyter notebook and Lazy\_load:

     * With the same Logging, we have 3 cases

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>User.objects.all()<br># this will print the sql<br>user_set=User.objecsts.all() <br># this will not print the sql<br><br>user_set=User.objecsts.all()<br>print(user_set)<br># this will print the sql<br></td></tr></tbody></table>

 * ## How to pretty print a class object and ignore typeerror only for dispalying: json.dumps and default=str

     * Best Method to pretty print an object:

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>from django.db import connections<br>import json<br>from pygments import highlight<br>from pygments.lexers import JsonLexer<br>from pygments.formatters import TerminalTrueColorFormatter<br><br>for c in connections.all():<br>    c_dict = {k: getattr(c, k) for k in dir(c)} # this gives all the properties listed using dir(c)<br>    json_str=json.dumps(c_dict, indent=4, sort_keys=True, default=str)<br>    print(highlight(json_str, JsonLexer(), TerminalTrueColorFormatter()))<br><br>For list of styles check the folder:<br>.venv/lib/python3.7/site-packages/pygments/styles<br>print(highlight(json_str, JsonLexer(), TerminalTrueColorFormatter(style='monokai')))<br>print(highlight(json_str, JsonLexer(), TerminalTrueColorFormatter(style='emacs')))<br>print(highlight(json_str, JsonLexer(), TerminalTrueColorFormatter(style=sas)))<br></td></tr></tbody></table>

 * ## dir() does much more than look up \_\_dict\_\_

     * https://stackoverflow.com/a/14361362/2897115

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>Python instances have their own __dict__, but so does their class:<br><br>&gt;&gt;&gt; class Foo(object):<br>...     bar = 'spam'<br>... <br>&gt;&gt;&gt; Foo().__dict__<br>{}<br>&gt;&gt;&gt; Foo.__dict__.items()<br>[('__dict__', &lt;attribute '__dict__' of 'Foo' objects&gt;), ('__weakref__', &lt;attribute '__weakref__' of 'Foo' objects&gt;), ('__module__', '__main__'), ('bar', 'spam'), ('__doc__', None)]<br>The dir() method uses both these __dict__ attributes, and the one on object to create a complete list of available attributes on the instance, the class, and on all ancestors of the class.<br><br><br></td></tr></tbody></table>

 * ## Python dictionary key error when assigning - how do I get around this?

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>myDict = {}<br>myDict[2000]['hello'] = 50<br>This is say key error:<br></td></tr></tbody></table>

     * KeyError occurs because you are trying to read a non-existant key when you try to access myDict\[2000\]. As an alternative, you could use defaultdict:

     * Solution:

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>&gt;&gt;&gt; from collections import defaultdict<br>&gt;&gt;&gt; myDict = defaultdict(dict)<br>&gt;&gt;&gt; myDict[2000]['hello'] = 50<br>&gt;&gt;&gt; myDict[2000]<br>{'hello': 50}<br><br>OR<br><br>myDict[2000] = {'hello': 50}<br></td></tr></tbody></table>

 * ## How to add dictionary items to list in python:

     * WRONG WAY:

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>&gt;&gt;&gt; dict = {}<br>&gt;&gt;&gt; list = []<br>&gt;&gt;&gt; for x in range(0,100):<br>...     dict[1] = x<br>...     list.append(dict)<br>... <br>&gt;&gt;&gt; print list<br></td></tr></tbody></table>

     * I would assume the result would be \[{1:1}, {1:2}, {1:3}... {1:98}, {1:99}\] but instead I got:

     * \[{1: 99}, {1: 99}, {1: 99}, {1: 99}, {1: 99}, {1: 99}, {1: 99}, {1: 99}, {1: 99}, {1: 99}, {1: 99}, … {1: 99}, {1: 99}\]

     * Any help is greatly appreciated.

     * THE RIGHT WAY 1:

     * You need to append a copy, otherwise you are just adding references to the same dictionary over and over again:

     * |                                                          |

     * | -------------------------------------------------------- |

     * | yourlist.append(yourdict.copy()) |

     * THE RIGHT WAY 2:

     * When you create the adict dictionary outside of the loop, you are appending the same dict to your alist list. It means that all the copies point to the same dictionary and you are getting the last value {1:99} every time. Just create every dictionary inside the loop and now you have your 100 different dictionaries.

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>alist = []<br>for x in range(100):<br>    adict = {1:x}<br>    alist.append(adict)<br>print(alist)<br></td></tr></tbody></table>

 * ## How to get the properties of an object:  

     * inspect.getmembers() vs \_\_dict\_\_ vs dir()

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>object.__dict__ =&gt; is a dictionary of the form {key: attribute, key2: atrribute2} etc.<br><br>dir(object)  =&gt; give list of strings =&gt; an alphabetized list of names comprising (some of) the attributes of the given object, and of attributes reachable from it.<br><br>inspect.getmembers() =&gt; give tuples =&gt; (name, attribute) instead of just the names.<br></td></tr></tbody></table>

     * To summarize, dir() and inspect.getmembers() are basically the same, while \_\_dict\_\_ is the complete namespace including metaclass attributes.

 * ## What are metaclasses in Python?

     * [https://stackoverflow.com/a/6581949/2897115](https://www.google.com/url?q=https://stackoverflow.com/a/6581949/2897115&sa=D&ust=1571383145295000)

     * First, you know that classes are objects that can create instances.

     * Well in fact, classes are themselves instances. Of metaclasses.

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>&gt;&gt;&gt; class Foo(object): pass<br>&gt;&gt;&gt; id(Foo)<br>142630324<br></td></tr></tbody></table>

     * Everything is an object in Python, and they are all either instances of classes or instances of metaclasses. Except for type.

 * ## Getting the sql of a query in  jupyter

     * ### 1) using mogrify from Psycopg extension

       * Using mogrify is best way but need to install Psycopg extension and will work only for postgresql DB. 

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>from django.db import connections<br>qs = User.objects.all()<br><br># Get a cursor tied to the default database<br>cursor = connections['default'].cursor() or <br>cursor = connections[qs.db].cursor()<br><br># Get the query SQL and parameters to be passed into psycopg2<br>query, params = qs.query.sql_with_params()<br><br># use mogrify: Return a query string after arguments binding. The string returned is exactly the one that would be sent to the database running the execute() method or similar.<br># mogrify is not a method defined by the Python DB API, but instead an add-on of the Psycopg driver. It does not exist for MySql<br>sql = cursor.mogrify(query, params)<br><br># Then format it using sqlparser and color it using pygment<br>import sqlparse<br>import pygments<br>from pygments.lexers import SqlLexer<br>from pygments.formatters import TerminalTrueColorFormatter<br># format using sqlparser<br>sql = sqlparse.format(sql, reindent=True)<br># color it using pygments<br>sql = pygments.highlight(sql,SqlLexer(),TerminalTrueColorFormatter())<br>#print it<br>print(sql)<br></td></tr></tbody></table>

       * OUTPUT

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>SELECT "custom_user_user"."id",<br>       "custom_user_user"."password",<br>       "custom_user_user"."last_login",<br>       "custom_user_user"."is_superuser",<br>       "custom_user_user"."is_staff",<br>       "custom_user_user"."date_joined",<br>       "custom_user_user"."first_name",<br>       "custom_user_user"."last_name",<br>       "custom_user_user"."email",<br>       "custom_user_user"."is_active",<br>       "custom_user_user"."about",<br>       "custom_user_user"."location",<br>       "custom_user_user"."birth_date",<br>       "custom_user_user"."email_confirmed",<br>       "custom_user_user"."jwt_secret",<br>       "custom_user_user"."otp_emailconfirm",<br>       "custom_user_user"."otp_passconfirm",<br>       "custom_user_user"."otp_loginconfirm",<br>       "custom_user_user"."otp_modified_date_emailconfirm",<br>       "custom_user_user"."otp_modified_date_passconfirm",<br>       "custom_user_user"."otp_modified_date_loginconfirm",<br>       "custom_user_user"."modified_date"<br>FROM "custom_user_user"<br></td></tr></tbody></table>

     * ### 2) Executing a new sql with EXPLAIN using cursor and then get the sql

       * [https://stackoverflow.com/a/47542953/2897115](https://www.google.com/url?q=https://stackoverflow.com/a/47542953/2897115&sa=D&ust=1571383145309000)

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>def str_query(qs):<br>    """<br>    qs.query returns something that isn't valid SQL, this returns the actual<br>    valid SQL that's executed: https://code.djangoproject.com/ticket/17741<br>    """<br>    cursor = connections[qs.db].cursor()<br>    query, params = qs.query.sql_with_params()<br>    cursor.execute('EXPLAIN ' + query, params)<br>    res = str(cursor.db.ops.last_executed_query(cursor, query, params))<br>    assert res.startswith('EXPLAIN ')<br>    return res[len('EXPLAIN '):]<br></td></tr></tbody></table>

     * ### 3) Using connections\[‘default’\].queries

       * https://stackoverflow.com/a/3748308/2897115

       * It should also be mentioned that if you have DEBUG = True, then all of your queries are logged, and you can get them by accessing connection.queries:

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>from django.db import connections<br>connections['default'].queries[-1]<br><br>Or<br><br>from django.db import connection<br>connection.queries[-1]<br></td></tr></tbody></table>

 * ## defaultdict() : assign default value when key does not exist

     * defaultdict means that if a key is not found in the dictionary, then instead of a KeyError being thrown, a new entry is created. The type of this new entry is given by the argument of defaultdict.

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>somedict = {} # It will be like Eg: { 'key' : 20}<br>print(somedict['test']) # KeyError because there is no key called ‘test’<br><br>someddict = defaultdict(int) # this means when we access any key which does not exist it will run print(int()) i.e print(0) i.e 0<br>print(somedict['test']) # print int(), thus 0<br></td></tr></tbody></table>

     * We use then when we dont know the keys and we want to add to the value of the key. 

     * We will have to run the code twice. First to assign 0 and later add the values. This will save time and help to attache a default value

     * Eg2:

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>somedict = {} # It will be like Eg: { 'key1' : { 'key21' : 40,  'key22' : 60 }}. Here we dont know key1, key21, key22, but we know that they will have float values<br><br>So<br><br>somedict = {'key1': defaultdict(float)}<br>somedict = defaultdict(floatdict)<br><br>floatdict(){<br> return defaultdict(float)<br>}<br><br>Somedict[‘keyunkown’][‘unknownkey’] = 0 ( it will not show key error)<br></td></tr></tbody></table>

 * ## counter(): collections — High-performance container datatypes

     * A Counter is a dict subclass for counting hashable objects. It is an unordered collection where elements are stored as dictionary keys and their counts are stored as dictionary values. Counts are allowed to be any integer value including zero or negative counts. 

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>queries = Counter()<br><br>Then <br>queries[q['sql']] += 1 (will not give any error)<br><br>The advantage of using collections is that they have some special functions. So counter has a function called most_common(int). So we can get the most common items 1 or 2 or 3 or whatever number we want.<br><br>duplicates = self.queries.most_common(1)<br><br>Eg: queries = { ‘type1’ : 5, ‘type3’: 6, ‘type2’: 10 etc}<br>Then queries.most_common(1) will give {‘type2’: 10}<br>Then queries.most_common(2) will give {‘type2’: 10, ‘type3’: 6,}<br></td></tr></tbody></table>

 * ## Python Concatenation (string + variables)

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>hello = "hello"<br>world = "world"<br><br>print hello + " " + world  # will work only if the variable is str type.<br>print "%s %s" % (hello, world)<br>print "{} {}".format(hello, world)<br>print ' '.join([hello, world])<br></td></tr></tbody></table>

 * ## How to get the project from git and start fresh

     * 1.  Take back up of the django\_basic\_documentation folder

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td># gauranga<br>cp -R /home/web_dev/django_basic_documentation /home/web_dev/backup_git/django_basic_documentation_backup_$(date +%Y-%m-%d-%H_%M_%S)  <br><br>The above will copy even the .gitignore files<br><br>OR best is<br><br>git clone /home/web_dev/django_basic_documentation /home/web_dev/backup_git/django_basic_documentation_backup_$(date +%Y-%m-%d-%H_%M_%S)<br></td></tr></tbody></table>

     * 2.  Delete everything inside /home/web\_dev/django\_basic\_documentation

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>#gauranga<br>Since we are using zsh so as per the comment below<br><a href="https://www.google.com/url?q=https://unix.stackexchange.com/questions/77127/rm-rf-all-files-and-all-hidden-files-without-error%23comment1001026_77313&amp;sa=D&amp;ust=1571383145329000" class="c24">https://unix.stackexchange.com/questions/77127/rm-rf-all-files-and-all-hidden-files-without-error#comment1001026_77313</a><br># rm -rf /home/web_dev/django_basic_documentation/*(D) <br></td></tr></tbody></table>

     * 3.  Cd into the directory and clone the git contents into the directory (Note: the directory as to be empty when we clone)

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>cd  /home/web_dev/django_basic_documentation/<br>git clone git@github.com:sant527/django_basic_documentation.git .<br>Warning: Permanently added the RSA host key for IP address '140.82.118.4' to the list of known hosts.<br>Enter passphrase for key '/home/simha/.ssh/id_rsa': <br>(it will ask for a password since we have set up ssh key)<br></td></tr></tbody></table>

     * 4.  Check git log

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>#gauranga<br>git --no-pager log --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)&lt;%an&gt;%Creset' --abbrev-commit<br></td></tr></tbody></table>

     * 5.  Install virtual env and activate it

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>#gauranga<br>export PIPENV_VENV_IN_PROJECT=1 (this will install virtual env in a .venv folder)<br><br>pipenv install<br><br>pipenv shell<br></td></tr></tbody></table>

     * 6.  Copy .env file to basic\_django (on git we dont commit the .env file so without it django will not runserver

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>#guranga<br>cp /home/web_dev/env_django_basic_documentation/.env /home/web_dev/django_basic_documentation/basic_django/basic_django/.env<br></td></tr></tbody></table>

     * 7.  cd django project folder and runserver

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>cd /home/web_dev/django_basic_documentation/basic_django/<br>python manage.py runserver<br></td></tr></tbody></table>

 * ## introspect properties and model fields in Django?

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>all_fields = User._meta.fields<br>#or<br>all_fields = User._meta.get_fields()<br><br>Note that:<br>all_fields=User._meta.get_fields()<br>Will also get some relationships,<br></td></tr></tbody></table>

     * Method 1:

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>def get_fields_and_properties(model, instance):<br>    field_names = [f.name for f in model._meta.fields]<br>    property_names = [name for name in dir(model) if isinstance(getattr(model, name), property)]<br>    return dict((name, getattr(instance, name)) for name in field_names + property_names)<br><br>instance = User()<br>print(get_fields_and_properties(User, instance))<br></td></tr></tbody></table>

     * Method 2:

     * |                                                                |

     * | -------------------------------------------------------------- |

     * | User.\_meta.\_\_dict\_\_.get("fields") |

     * Method: 

     * Django extensions

     * https://django-extensions.readthedocs.io/en/latest/command\_extensions.html

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>$ python manage.py describe_form custom_user.User<br><br>from django import forms<br>from custom_user.models import User<br><br>class UserForm(forms.Form):<br>    password = forms.CharField(label='Password', max_length=128)<br>    last_login = forms.DateTimeField(label='Last login', required=False)<br>    is_superuser = forms.BooleanField(help_text='Designates that this user has all permissions without explicitly assigning them.', initial=False, label='Superuser status', required=False)<br>    is_staff = forms.BooleanField(help_text='Designates whether the user can log into this admin site.', initial=False, label='Staff status', required=False)<br>    date_joined = forms.DateTimeField(initial=&lt;function now at 0x7f7a3aba07b8&gt;, label='Date joined')<br>    first_name = forms.CharField(label='First name', max_length=30)<br>    last_name = forms.CharField(label='Last name', max_length=150)<br>    email = forms.EmailField(help_text='Please Enter valid Email Address', label='Email address', max_length=254)<br>    is_active = forms.BooleanField(help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', initial=False, label='Active', required=False)<br>    about = forms.CharField(label='About', max_length=500, required=False)<br>    location = forms.CharField(label='Location', max_length=30, required=False)<br>    birth_date = forms.DateField(label='Birth date', required=False)<br>    email_confirmed = forms.BooleanField(initial=False, label='Email confirmed', required=False)<br>    otp_emailconfirm = forms.CharField(help_text='Please Enter valid OTP sent to your Email', label='Otp', max_length=6)<br>    otp_passconfirm = forms.CharField(help_text='Please Enter valid OTP sent to your Email', label='Otp', max_length=6)<br>    otp_loginconfirm = forms.CharField(help_text='Please Enter valid OTP sent to your Email', label='Otp', max_length=6)<br>    otp_modified_date_emailconfirm = forms.DateTimeField(label='Otp modified date emailconfirm')<br>    otp_modified_date_passconfirm = forms.DateTimeField(label='Otp modified date passconfirm')<br>    otp_modified_date_loginconfirm = forms.DateTimeField(label='Otp modified date loginconfirm')<br>    groups = forms.ModelMultipleChoiceField(help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', label='Groups', required=False)<br>    user_permissions = forms.ModelMultipleChoiceField(help_text='Specific permissions for this user.', label='User permissions', required=False)<br></td></tr></tbody></table>

 * ## Django render a template

     * Put the following code in that template:

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>polls/templates/polls/index.html¶<br>{% if latest_question_list %}<br>    &lt;ul&gt;<br>    {% for question in latest_question_list %}<br>        &lt;li&gt;&lt;a href="/polls/{{ question.id }}/"&gt;{{ question.question_text }}&lt;/a&gt;&lt;/li&gt;<br>    {% endfor %}<br>    &lt;/ul&gt;<br>{% else %}<br>    &lt;p&gt;No polls are available.&lt;/p&gt;<br>{% endif %}<br></td></tr></tbody></table>

     * Now let’s update our index view in polls/views.py to use the template:

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>polls/views.py¶<br>from django.http import HttpResponse<br>from django.template import loader<br><br>from .models import Question<br><br><br>def index(request):<br>    latest_question_list = Question.objects.order_by('-pub_date')[:5]<br>    template = loader.get_template('polls/index.html')<br>    context = {<br>        'latest_question_list': latest_question_list,<br>    }<br>    return HttpResponse(template.render(context, request))<br></td></tr></tbody></table>

     * That code loads the template called polls/index.html and passes it a context. The context is a dictionary mapping template variable names to Python objects.

     * Load the page by pointing your browser at “/polls/”, and you should see a bulleted-list containing the “What’s up” question from Tutorial 2. The link points to the question’s detail page.

     * ### A shortcut: render()

       * It’s a very common idiom to load a template, fill a context and return an HttpResponse object with the result of the rendered template. Django provides a shortcut. Here’s the full index() view, rewritten:

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>polls/views.py¶<br>from django.shortcuts import render<br><br>from .models import Question<br><br><br>def index(request):<br>    latest_question_list = Question.objects.order_by('-pub_date')[:5]<br>    context = {'latest_question_list': latest_question_list}<br>    return render(request, 'polls/index.html', context)<br></td></tr></tbody></table>

       * Note that once we’ve done this in all these views, we no longer need to import loader and HttpResponse (you’ll want to keep HttpResponse if you still have the stub methods for detail, results, and vote).

       * The render() function takes the request object as its first argument, a template name as its second argument and a dictionary as its optional third argument. It returns an HttpResponse object of the given template rendered with the given context.

     * ### Raising a 404 error¶

       * Now, let’s tackle the question detail view – the page that displays the question text for a given poll. Here’s the view:

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>polls/views.py¶<br>from django.http import Http404<br>from django.shortcuts import render<br><br>from .models import Question<br># ...<br>def detail(request, question_id):<br>    try:<br>        question = Question.objects.get(pk=question_id)<br>    except Question.DoesNotExist:<br>        raise Http404("Question does not exist")<br>    return render(request, 'polls/detail.html', {'question': question})<br></td></tr></tbody></table>

       * The new concept here: The view raises the Http404 exception if a question with the requested ID doesn’t exist.

       * We’ll discuss what you could put in that polls/detail.html template a bit later, but if you’d like to quickly get the above example working, a file containing just:

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>polls/templates/polls/detail.html¶<br>{{ question }}<br></td></tr></tbody></table>

       * will get you started for now.

     * ### A shortcut: get\_object\_or\_404()¶

       * It’s a very common idiom to use get() and raise Http404 if the object doesn’t exist. Django provides a shortcut. Here’s the detail() view, rewritten:

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>polls/views.py¶<br>from django.shortcuts import get_object_or_404, render<br><br>from .models import Question<br># ...<br>def detail(request, question_id):<br>    question = get_object_or_404(Question, pk=question_id)<br>    return render(request, 'polls/detail.html', {'question': question})<br></td></tr></tbody></table>

       * The get\_object\_or\_404() function takes a Django model as its first argument and an arbitrary number of keyword arguments, which it passes to the get() function of the model’s manager. It raises Http404 if the object doesn’t exist.

     * ### Philosophy

       * Why do we use a helper function get\_object\_or\_404() instead of automatically catching the ObjectDoesNotExist exceptions at a higher level, or having the model API raise Http404 instead of ObjectDoesNotExist?

       * Because that would couple the model layer to the view layer. One of the foremost design goals of Django is to maintain loose coupling. Some controlled coupling is introduced in the django.shortcuts module.

       * There’s also a get\_list\_or\_404() function, which works just as get\_object\_or\_404() – except using filter() instead of get(). It raises Http404 if the list is empty.

 * ## Passing variables between views:

     * Use sessions

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>For setting session variable:<br>request.session['fav_color'] = 'blue'<br><br>For getting session Data<br>fav_color = request.session.get('fav_color', 'red')<br></td></tr></tbody></table>

 * ## Want to check if a key is set in session

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>if 'name' in request.session:<br>    print request.session['name']<br><br>Or<br><br>You can use the get-method on the session dictionary, it will not throw an error if the key doesn't exist, but return none as a default value or your custom default value:<br><br>cart = request.session.get('cart')<br>cart = request.session.get('cart', 'no cart')<br><br>Or<br><br>if 'cart' not in request.session:<br></td></tr></tbody></table>

 * ## Using redirect() to redirect to another view

     * redirect(to, \*args, permanent=False, \*\*kwargs) = HttpResponseRedirect(reverse(viewname, urlconf=None, args=None, kwargs=None, current\_app=None))

     * Here viewname is based on URL Namespace. For that define app\_name at app level and name at url level

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>from django.urls import reverse<br><br>def myview(request):<br>    return HttpResponseRedirect(reverse('arch-summary', args=[1945]))<br></td></tr></tbody></table>

     * You can also pass kwargs instead of args. For example:

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>&gt;&gt;&gt; reverse('admin:app_list', kwargs={'app_label': 'auth'})<br>'/admin/auth/'<br></td></tr></tbody></table>

     * args and kwargs cannot be passed to reverse() at the same time.

     * If no match can be made, reverse() raises a NoReverseMatch exception.

 * ## URL Namespace

     * [https://docs.djangoproject.com/en/2.2/topics/http/urls/\#url-namespaces](https://www.google.com/url?q=https://docs.djangoproject.com/en/2.2/topics/http/urls/%23url-namespaces&sa=D&ust=1571383145372000)

     * Namespace’s are defined at three levels:

     * In the below examples we can see:

     * Include - namespace = 'test-polls' (We use this when we use the same app multiple times like)

     *                  path('author-polls/', include('polls.urls', namespace='author-polls')),

     *                  path('publisher-polls/', include('polls.urls', namespace='publisher-polls')),

     * App leve - app\_name = 'polls'

     * Url\_leve - name = 'index'

     * urls.py

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>from django.urls import include, path<br><br>urlpatterns = [<br>    path(‘polls/', include('polls.urls', namespace='test-polls')),<br>]<br></td></tr></tbody></table>

     * polls/urls.py

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>from django.urls import path<br>from . import views<br><br>app_name = 'polls'<br>urlpatterns = [<br>    path('', views.IndexView.as_view(), name='index'),<br>    path('&lt;int:pk&gt;/', views.DetailView.as_view(), name='detail'),<br>    ...<br>]<br></td></tr></tbody></table>

     * How to mention polls\>index

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>reverse(‘polls:index’) <br>reverse(‘test-polls:index’)<br></td></tr></tbody></table>

     * For complex scenarios refer: https://docs.djangoproject.com/en/2.2/topics/http/urls/\#id5

     *  

     * Passing variables between views:

     * 1.  Encode it in the URL

     * 2.  Using hidden form elements

     * https://stackoverflow.com/questions/52358128/how-to-pass-data-from-one-view-to-the-next

     * 3.  Using session variables and/or cookies

     * Assuming you've activated django.contrib.sessions.middleware.SessionMiddleware; you can pass data between views using request.session dictionary as follows:

 * ## Messages Django:

     * [https://www.youtube.com/watch?v=3kGv8naG7wY](https://www.google.com/url?q=https://www.youtube.com/watch?v%3D3kGv8naG7wY&sa=D&ust=1571383145380000)

     * Example we have a 

 * ## os.environ.setdefault('DJANGO\_SETTINGS\_MODULE', 'basic\_django.settings') - will not modify/create new shell Env variables.

     * https://stackoverflow.com/a/27876270/2897115

     * The dictionary os.environ contains the environment variables that the python process was spawned with, from the shell it was spawned in.

     * The piece of code os.environ.setdefault('foo', 'bar') tells this dictionary to provide the value 'bar' when looking up the ke 'foo'. This has nothing to do with the environment variables that the python process was started with, as creation of the os.environ dictionary is a one-way trip. The os.environ is not some kind of "reference" to a dictionary of the environment variables of your process, it's a copy of that. As such, modifying it has no effect in the shell.

 * ## Python Relative and Absolute Import

     * [https://blog.tankywoo.com/python/2013/10/07/python-relative-and-absolute-import.html](https://www.google.com/url?q=https://blog.tankywoo.com/python/2013/10/07/python-relative-and-absolute-import.html&sa=D&ust=1571383145382000)

 * ## Decorators Python

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>def my_decorator(func):<br>    def wrapper():<br>        print("Something is happening before the function is called.")<br>        func()<br>        print("Something is happening after the function is called.")<br>    return wrapper<br><br>@my_decorator<br>def say_whee():<br>    print("Whee!")<br><br>When some one calls <br>say_whee()<br><br>Is equivalent to<br><br>say_whee = my_decorator(say_whee)<br>say_whee()<br><br>&gt;&gt;&gt; say_whee()<br>Something is happening before the function is called.<br>Whee!<br>Something is happening after the function is called.<br><br>Also check:<br>&gt;&gt;&gt; say_whee<br>&lt;function my_decorator.&lt;locals&gt;.wrapper at 0x7f3c5dfd42f0&gt;<br></td></tr></tbody></table>

 * ## Celery and Redis

     * Install redis

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>pacman -S redis<br>Then <br>redis-server<br></td></tr></tbody></table>

     * Celery worker and your application/script are different processes and run independent of each other. So your application/script and celery need some way to communicate with each other. That’s where a message queue comes into picture.

     * Application code needs to put the task somewhere from where celery worker can fetch it and execute. Application code puts the task on a message queue. Celery worker fetches the task from message queue and exectues the task. We will use redis as the message queue.

     * This example is for non django

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>mkdir celery_test<br>cd celery_test<br>export PIPENV_VENV_IN_PROJECT=1<br>pipenv install<br>pipenv shell<br>pipenv install celery redis ipython<br><br>then create a file called tasks.py<br><br>And put:<br>from celery import Celery<br><br># Create a celery application (the first argument is the name of the module)<br><br>redis = 'redis://localhost:6379/'<br>app = Celery('proj', broker=redis, backend=redis)<br><br>Or<br><br>app = Celery('tasks', broker='redis://localhost:6379/0')<br><br># Add a task to the application<br>@app.task<br>def add(x, y):<br>    return x + y<br><br>## Celery will add the task to its queue ("worker, please call myapp.tasks.add(2, 2)") and return immediately. As soon as an idle worker sees it at the head of the queue, the worker will remove it from the queue, then execute it:<br><br><br>Or<br><br>#Celery creates task names based on how module is imported. It is a little dangerous. Set explicitly name for every task.<br>#Prefer using proj.package.module.function_name convention to avoid collisions with 3rd party packages.<br><br>@app.task(name='proj.package.tasks.add')<br>def add(a, b):<br>    return a + b<br><br># Put the task in the queue, you send a task request to a broker (most commonly redis)<br># when workers finish they put their results back<br>add.delay(2, 2) is same as<br><br>Or<br><br>add.apply_async(args=(4, 5)) OR<br>add.apply_async(queue='high_priority', priority=0, kwargs={'a': 10, 'b': 5})<br>https://pawelzny.com/python/celery/2017/08/14/celery-4-tasks-best-practices/<br><br># (The -A option allows us to specify the module we want to run)<br>#  the worker controls 5 processes. The worker distributes tasks among the 5 processes.<br>celery worker -A tasks --loglevel=info --concurrency 5<br></td></tr></tbody></table>

     * [https://www.caktusgroup.com/blog/2014/06/23/scheduling-tasks-celery/](https://www.google.com/url?q=https://www.caktusgroup.com/blog/2014/06/23/scheduling-tasks-celery/&sa=D&ust=1571383145397000)

     * THEORY:

     * A task is just a Python function.

     * We'll set up Celery so that your tasks run in pretty much the same environment as the rest of your application's code, so they can access the same database and Django settings.

     * When a task is ready to be run, Celery puts it on a queue, a list of tasks that are ready to be run.

     * You can have many queues, but we'll assume a single queue here for simplicity.

     * Putting a task on a queue just adds it to a to-do list, so to speak. In order for the task to be executed, some other process, called a worker, has to be watching that queue for tasks. When it sees tasks on the queue, it'll pull off the first and execute it, then go back to wait for more. You can have many workers, possibly on many different servers, but we'll assume a single worker for now.

     * Can Set name for every task

     * https://pawelzny.com/python/celery/2017/08/14/celery-4-tasks-best-practices/

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>Celery creates task names based on how module is imported. It is a little dangerous. Set explicitly name for every task. Prefer using proj.package.module.function_name convention to avoid collisions with 3rd party packages.<br><br>@app.task(name='proj.package.tasks.add')<br>def add(a, b):<br>    return a + b<br></td></tr></tbody></table>

     * ### For Django

       * pipenv install celery redis  \#install celery and redis

       * In main project app, next to settings.py, create new module celery.py.

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>proj<br>|-- proj<br>|   |-- __init__.py<br>|   |-- celery.py<br>|   |-- settings.py<br>|   |-- tasks.py<br>|   |-- urls.py<br>|-- manage.py<br>|-- requirements.txt<br><br><br>from celery import Celery<br><br>os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'basic_django.settings')<br># without this the os.environ.setdefault, below will not be noticed in settings.py<br># CELERY_IMPORTS = (<br>#     'login_register_password.tasks',<br># )<br># And without mentioning the imports it will not show in the tasks  it will show error  Received unregistered task <br><br><br>redis = 'redis://localhost:6379/'<br>app = Celery('proj', broker=redis, backend=redis)<br><br>#Celery instance is assign to app variable by convention. Keep your project simple and #consistent. Celery instance should be named same as project.<br><br>#For example if project’s name is “gift-catalogue” then app = Celery('gift-catalogue', broker=redis, backend=redis)<br></td></tr></tbody></table>

       * To proj/proj/\_\_init\_\_.py add this lines to load celery on Django startup:

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>from proj.celery import app as celery_app<br><br>## __all__ affects how from ... import * works.<br>## import * is to import all symbols that do not begin with an underscore,<br>## It is a list of strings defining what symbols in a module will be exported when from &lt;module&gt; import * is used on the module.<br>__all__ = ['celery_app']<br></td></tr></tbody></table>

       * Add to settings.py

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td># mention here where are the tasks are defined better store apps in app/tasks.py<br>CELERY_IMPORTS = (<br>    'path wherever the tasks are defined',<br>)<br></td></tr></tbody></table>

       * From now on we can call tasks with delay() OR apply\_async() methods.

       * Create proj/app/tasks.py

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>from proj import celery_app<br><br>#Note use name: <br># it's important that your task is always imported and refered to using the same package name. For example, depending on how your Python path is set up, it might be possible to refer to it as either myproject.myapp.tasks.add or myapp.tasks.add. Or from myapp.views, you might import it as .tasks.add. But Celery has no way of knowing those are all the same task.<br># <a href="https://www.google.com/url?q=https://www.caktusgroup.com/blog/2014/06/23/scheduling-tasks-celery/&amp;sa=D&amp;ust=1571383145407000" class="c24">https://www.caktusgroup.com/blog/2014/06/23/scheduling-tasks-celery/</a><br># And also from https://pawelzny.com/python/celery/2017/08/14/celery-4-tasks-best-practices/<br>#Celery creates task names based on how module is imported. It is a little dangerous. Set explicitly name for every task. Prefer using proj.package.module.function_name convention to avoid collisions with 3rd party packages.<br><br>@celery_app.task(name='proj.package.tasks.add')<br>def add(a, b):<br>    return a + b<br><br>add.delay(4, 5) <br><br>OR<br>add.apply_async(args=(4, 5))<br><br>OR more detailed<br><br>add.apply_async(queue='high_priority', priority=0, kwargs={'a': 10, 'b': 5})<br><a href="https://www.google.com/url?q=https://pawelzny.com/python/celery/2017/08/14/celery-4-tasks-best-practices/&amp;sa=D&amp;ust=1571383145410000" class="c24">https://pawelzny.com/python/celery/2017/08/14/celery-4-tasks-best-practices/</a><br><br>Ofcourse for this we have to run celery as<br>celery -A proj worker -l info -Q high_priority -c 4<br><br>OR<br><br>celery -A proj worker -l info -Q high_priority --autoscale 8,4<br></td></tr></tbody></table>

       * Enable virtualenv with installed celery then be sure you are in root project directory. You have to be one directory above main app directory, exactly where manage.py is.

       * Run worker with -A proj argument where proj is your main django app directory name, where celery.py exists.

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>celery -A proj worker -l info<br><br>OR<br><br>celery -A proj worker -l info -c 4 <br>## (-c parameter defines how many concurrent threads worker create.)<br></td></tr></tbody></table>

     * ### Shared\_task vs task

       * https://groups.google.com/forum/\#\!topic/celery-users/XiSDiNjBR6k

       * [https://stackoverflow.com/questions/21233089/how-to-use-the-shared-task-decorator-for-class-based-tasks](https://www.google.com/url?q=https://stackoverflow.com/questions/21233089/how-to-use-the-shared-task-decorator-for-class-based-tasks&sa=D&ust=1571383145414000)

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>from proj import celery_app<br><br>@celery_app.task<br>def add(a, b):<br>    return a + b<br><br>VS<br><br>from celery import shared_task<br><br>@shared_task<br>def foo():<br>    Pass<br><br>The @shared_task decorator lets you create tasks that can be used by any app(s).<br></td></tr></tbody></table>

 * ## Flower: Real-time Celery web-monitor

     * pipenv install flower

     * celery -A proj flower

     * The default port is http://localhost:5555, but you can change this using the –port argument:

     * $ celery -A proj flower --port=5555

 * ## Django Authentication:

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>from django.contrib.auth import authenticate, login<br><br>def my_view(request):<br>    username = request.POST['username']<br>    password = request.POST['password']<br>    user = authenticate(username=username, password=password)<br>    if user is not None:<br>        if user.is_active:<br>            login(request, user)<br>            # Redirect to a success page.<br>        else:<br>            # Return a 'disabled account' error message<br>            ...<br>    else:<br>        # Return an 'invalid login' error message.<br>        ...<br></td></tr></tbody></table>

     * LOGIN vs AUTHENTICATE

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>authenticate just verifies the login information.  login will take the user object and set the cookies<br><br>To further clarify, authentication is a one-time check, and doesn't imply a login session. A login session implies some period of time during which the user is free to perform various restricted activities without repeated authentication checks.<br><br>Authenticate refers to verifying the user credentials Whereas login refers to creation of a user session once the user credentials has been verified(authenticated)<br></td></tr></tbody></table>

     * AUTHENTICATION vs AUTHORIZATION

     * https://docs.djangoproject.com/en/2.2/topics/auth/\#overview

     * |                                                                                                                                                                                                                                                                                                                 |

     * | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

     * | The Django authentication system handles both authentication and authorization. Briefly, authentication verifies a user is who they claim to be, and authorization determines what an authenticated user is allowed to do. Here the term authentication is used to refer to both tasks. |

 * ## How to log a user in

     * [https://docs.djangoproject.com/en/2.2/topics/auth/default/\#how-to-log-a-user-in](https://www.google.com/url?q=https://docs.djangoproject.com/en/2.2/topics/auth/default/%23how-to-log-a-user-in&sa=D&ust=1571383145423000)

     * If you have an authenticated user you want to attach to the current session - this is done with a login() function.

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>from django.contrib.auth import authenticate, login<br><br>def my_view(request):<br>    username = request.POST['username']<br>    password = request.POST['password']<br>    user = authenticate(request, username=username, password=password)<br>    if user is not None:<br>        login(request, user)<br>        # Redirect to a success page.<br>        ...<br>    else:<br>        # Return an 'invalid login' error message.<br>        ...<br></td></tr></tbody></table>

     * When a user logs in, the user’s ID and the backend that was used for authentication are saved in the user’s session. This allows the same authentication backend to fetch the user’s details on a future request. The authentication backend to save in the session is selected as follows:

     * Use the value of the user.backend attribute, if present. This allows pairing authenticate() and login(): authenticate() sets the user.backend attribute on the user object it returns.

 * ## How to log a user out¶

     * [https://docs.djangoproject.com/en/2.2/topics/auth/default/\#how-to-log-a-user-out](https://www.google.com/url?q=https://docs.djangoproject.com/en/2.2/topics/auth/default/%23how-to-log-a-user-out&sa=D&ust=1571383145428000)

     * logout(request)\[source\]¶

     * To log out a user who has been logged in via django.contrib.auth.login(), use django.contrib.auth.logout() within your view. It takes an HttpRequest object and has no return value. Example:

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>from django.contrib.auth import logout<br>def logout_view(request):<br>    logout(request)<br>    # Redirect to a success page.<br></td></tr></tbody></table>

     * Note that logout() doesn’t throw any errors if the user wasn’t logged in.

     * When you call logout(), the session data for the current request is completely cleaned out. All existing data is removed. This is to prevent another person from using the same Web browser to log in and have access to the previous user’s session data. If you want to put anything into the session that will be available to the user immediately after logging out, do that after calling django.contrib.auth.logout().

 * ## Retrieving all field instances of a model (\_meta)

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td># include hidden fields and also include_parents=True is default, So all parent fields are also included.<br>&gt;&gt;&gt; User._meta.get_fields(include_hidden=True)<br>(&lt;ManyToOneRel: auth.user_groups&gt;,<br> &lt;ManyToOneRel: auth.user_user_permissions&gt;,<br> &lt;ManyToOneRel: admin.logentry&gt;,<br> &lt;django.db.models.fields.AutoField: id&gt;,<br> &lt;django.db.models.fields.CharField: password&gt;,<br> &lt;django.db.models.fields.DateTimeField: last_login&gt;,<br> &lt;django.db.models.fields.BooleanField: is_superuser&gt;,<br> &lt;django.db.models.fields.CharField: username&gt;,<br> &lt;django.db.models.fields.CharField: first_name&gt;,<br> &lt;django.db.models.fields.CharField: last_name&gt;,<br> &lt;django.db.models.fields.EmailField: email&gt;,<br> &lt;django.db.models.fields.BooleanField: is_staff&gt;,<br> &lt;django.db.models.fields.BooleanField: is_active&gt;,<br> &lt;django.db.models.fields.DateTimeField: date_joined&gt;,<br> &lt;django.db.models.fields.related.ManyToManyField: groups&gt;,<br> &lt;django.db.models.fields.related.ManyToManyField: user_permissions&gt;)<br></td></tr></tbody></table>

 * ## Django's Built in Authentication

     * [https://dev.to/apcelent/json-web-token-based-authentication-backend-for-django-project-3n90](https://www.google.com/url?q=https://dev.to/apcelent/json-web-token-based-authentication-backend-for-django-project-3n90&sa=D&ust=1571383145434000)

     * Django has session and authentication management built-in. It takes care of session and auth via Middlewares, that modify incoming requests and outgoing responses.

     * Django Session Middleware takes an incoming request looks for a session key in the request’s cookies, and then sets request.session to a SessionStore instance. If the request session is modified, or if the configuration is to save the session every time, it saves the changes and sets a session cookie or deletes if the session has been emptied.

     * The Auth Middleware sets request.user to a LazyUser. LazyUser here is being used to delay the instantiation of the wrapped class. When request.user is accessed – say by @login\_required decorator – LazyUser calls django.contrib.auth.get\_user(), passing in the request; get\_user() pulls information out of the session and, if the user is authenticated, returns the appropriate User instance. However, if there is no session details for the user, an attempt is made to authenticate the user.

     * How do we authenticate the user?

     * Given a dict of credentials(username and password) we call the django.contrib.auth.autenticate(\*\*credentials). This function returns the User object, if successful, or None if credentials were not correct.

     * Given an authenticated User object, we call the django.contrib.auth.login(request, user). This stores the authentication backend and the user's id into the session. Since, one of the variable in session stands modified, request.session should be updated, this is done by process\_response in Session Middleware.

     * Example of custom authentication backend

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>Let's implement a basic custom auth backend, where password of all the user's is alphaQ.<br><br>Username: alpha Password: alphapass<br><br>    # import the User object<br>    from django.contrib.auth.models import User<br><br>    # Define backend class<br>    class BasicCustomBackend(object):<br><br>        # Create an authentication method<br>        def authenticate(self, username=None, password=None):<br><br>        try:<br>            # Try to find a user matching the username provided<br>            user = User.objects.get(username=username)<br><br>            # if successful return user if not return None<br>            if password == 'alphapass':<br>                return user<br>            else:<br>                return None<br>        except User.DoesNotExist:<br>            # No user was found<br>            return None<br><br>        # Required for the backend to work properly<br>        def get_user(self, user_id):<br>        try:<br>            return User.objects.get(pk=user_id)<br>        except User.DoesNotExist:<br>            return None<br></td></tr></tbody></table>

 * ## Application Configuration feature someapp.apps.AppConfig

     * That is the Application Configuration feature, new to Django 1.7.

     * Basically, now you can list in INSTALLED\_APPS either the module that contains the application or a class that derives from django.apps.AppConfig and defines the behavior of the application.

     * [https://stackoverflow.com/a/34377341/2897115](https://www.google.com/url?q=https://stackoverflow.com/a/34377341/2897115&sa=D&ust=1571383145441000)

     * This feature provides several advantages:

     * Apps can be configured more easily, and even subclassed for customization.

     * You can have several apps in the same module.

     * Application modules can define the special module variable default\_app\_config to specify the name of their AppConfig, so that they can use the new features without having to specify the full name of that class in INSTALLED\_APPS. But this is a backwards compatibility feature and new applications are recommended to write the full AppConfig name.

     * Anyway, most django/contrib apps use that default\_app\_config, for compatibility with old configurations. See for example the file django/contrib/messages/\_\_init\_\_.py is just:

     * from django.contrib.messages.api import \*

     * from django.contrib.messages.constants import \*

     * default\_app\_config = 'django.contrib.messages.apps.MessagesConfig'

     * So, adding it up, per OP request:

     * If you add in INSTALLED\_APPS the typename foo.apps.FooConfig, then that class will be used to setup the foo app, 1.7 style (recommended).

     * If you add in INSTALLED\_APPS the plain name foo, then:

     * if there is a variable foo.default\_app\_config this class will be used to setup the foo app, 1.7 style. Most (all?) the standard Django apps have this variable, so that you don't need to change your INSTALLED\_APPS when you upgrade from Django-1.6 to Django-1.7.

     * if there is not such a variable, then the 1.6 style application will be used, with default values for the advanced configuration options.

 * ## DJANGO SECRET\_KEY:

     * This value \[the SECRET\_KEY setting\] is the key to securing signed data – it is vital you keep this secure, or attackers could use it to generate their own signed values.

     * It uses for csrf\_token

     * Sessions: encrypting and/or hashing cookies data,

     * Unique tokens for a user session, password reset request, messages, etc.

 * ## Why dont we see the session variable in the chrome:

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>Yes. Unless you have specifically set the session backend to use cookies, the data is stored in the database and only a key is stored in the cookie.<br><br>The session is stored in the database, not in the user's cookie. There is no way for the user to change that data. The only thing stored in the cookie is the hash of the session ID itself.<br></td></tr></tbody></table>

     * If we set a session variable:

     * request.session\['test'\] = id

     * When we see the chrome we see:

     * ![](images/image204.png)

     * So here we dont see the session varible test.

     * Django sends onlt the session id as a cookie and stores the rest in the database.

 * ## In the template user is available 

 * ## What is need to login a user

     * authenticate method does not save the authenticated user in session

     * So one need to use login method after authentication from the same module

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>def authenticate(request=None, **credentials):<br>    """<br>    If the given credentials are valid, return a User object.<br>    """<br><br>def login(request, user, backend=None):<br>    """<br>    Persist a user id and a backend in the request. This way a user doesn't<br>    have to reauthenticate on every request. Note that data set during<br>    the anonymous session is retained when the user logs in.<br>    """<br></td></tr></tbody></table>

 * ## Django - allow url only to be accessed from a specific page

     * We dont want enter otp page directly. We want to be accessed only after the email form page.

 * ## Logging does not work in try: except: 

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>Try:<br>   Something<br>    logging.debug()<br>Except: <br>    <br></td></tr></tbody></table>

     * If there is an exception then logging.debug will not work

 * ## \`if key in dict\` vs. \`try/except\` - which is more readable idiom?

     * [https://stackoverflow.com/questions/4512557/if-key-in-dict-vs-try-except-which-is-more-readable-idiom](https://www.google.com/url?q=https://stackoverflow.com/questions/4512557/if-key-in-dict-vs-try-except-which-is-more-readable-idiom&sa=D&ust=1571383145451000)

     * I think the general rule here is will A\["blah"\] normally exist, if so try-except is good if not then use if "blah" in b:

 * ## Datetime using timezone when passing data using session or json

     * Best way to get current datetime with timezone aware is (here we are not converting time to different time zone. Python will get the current local time and append the time zone mentioned. For getting the same time in different timezone we have to use astimezone.

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>Import datetime<br># gauranga<br># datetime.datetime.now(tz=timezone)<br>str(datetime.datetime.now(tz=pytz.timezone("America/New_York")))<br><br>If we try tz='America/New_York' instead of tz=pytz.timezone("America/New_York") we get<br><br>str(datetime.datetime.now(tz='America/New_York'))<br>TypeError: tzinfo argument must be None or of a tzinfo subclass, not type 'str'<br><br>Or<br><br>datetime.datetime(2009, 7, 10, 18, 44, 59, 193982, tzinfo=pytz.timezone("America/New_York"))<br>Tzinfo should be  tzinfo subclass.<br><br>Also note: there is another way if we know the time gap<br>tz = datetime.timezone.utc <br>repr(tz)<br><br>tz = datetime.timezone(datetime.timedelta(hours=-5), 'ANYSTRING')<br>repr(tz)<br># "datetime.timezone(datetime.timedelta(days=-1, seconds=68400), 'ANYSTRING')"<br>## whats the difference<br><br>str(datetime.datetime.now())<br># '2019-10-04 04:18:46.966622'<br><br>str(datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=-5), 'ANYSTRING')))<br># '2019-10-03 23:20:24.052399-05:00'<br><br>Whereas:<br><br>str(datetime.datetime.now())<br># '2019-10-04 04:21:17.492501'<br><br>str(datetime.datetime.now(tz=pytz.timezone("America/New_York")))<br># '2019-10-04 00:21:35.434944-04:00'<br><br>tz=pytz.timezone("America/New_York") time is not changed only timezone is appended where whereas with tz=datetime.timezone(datetime.timedelta(hours=-5), 'ANYSTRING')) local time changed and timezone is appended. <br><br>Similarly:<br><br>str(datetime.datetime(2009, 7, 10, 18, 44, 59, 193982))<br>'2009-07-10 18:44:59.193982'<br><br> str(datetime.datetime(2009, 7, 10, 18, 44, 59, 193982, tzinfo=datetime.timezone(datetime.timedelta(hours=-5), 'ANYSTRING')))<br>#'2009-07-10 18:44:59.193982-05:00'<br><br>str(datetime.datetime(2009, 7, 10, 18, 44, 59, 193982, tzinfo=pytz.timezone("America/New_York")))<br>'2009-07-10 18:44:59.193982-04:56'<br><br>We observe the 2009-07-10 18:44:59.193982 does not change only the timezone appending changes<br><br></td></tr></tbody></table>

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>import datetime<br>import pytz<br># pytz.utc is pytz.UTC is pytz.timezone('UTC')<br><br>unaware = datetime.datetime.now()<br>str(unaware)<br># '2019-10-04 02:49:41.572484'<br><br>now_aware = unaware.replace(tzinfo=pytz.timezone('UTC'))<br>str(now_aware)<br># '2019-10-04 02:49:41.572484+00:00'<br><br>now_aware = unaware.replace(tzinfo=pytz.timezone('Asia/Kolkata'))<br>str(now_aware)<br># '2019-10-04 02:49:41.572484+05:53'<br><br># Note that replace only adds the +thing or timezone info. It does not change the time<br><br>#If we want to see the same time as in different timezone then<br>str(now_aware.astimezone(pytz.timezone('Europe/Amsterdam')))<br>#'2019-10-03 22:56:41.572484+02:00'<br><br>str(now_aware.astimezone(pytz.timezone('Asia/Kolkata')))<br># '2019-10-04 02:49:41.572484+05:53'<br><br></td></tr></tbody></table>

 * ## Convert datetime string to python datetime

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>Use fromisoformat for python &gt; 3.7<br>datetime.datetime.fromisoformat('2019-10-04T04:06:46.051628-04:00')<br><br>Or<br><br>datetime.datetime.strptime("2019-10-04T04:06:46.051628-04:00", "%Y-%m-%dT%H:%M:%S.%f%z")<br><br>%Y        Year with century as a decimal number.        0001, 0002, … , 9999<br>%m        Month as a zero-padded decimal number.        01, 02 … 12<br>%d        Day of the month as a zero-padded decimal number.        01, 02, …, 31<br>%H        Hour (24-hour clock) as a zero-padded decimal number.        01, 02, … , 23<br>%M        Minute as a zero-padded decimal number.        01, 02, … , 59<br>%S        Second as a zero-padded decimal number.        01, 02, … , 59<br>%f        Microsecond as a decimal number, zero-padded on the left.        000000, 000001, …, 999999<br>%z        UTC offset in the form ±HHMM[SS] (empty string if the object is naive).        (empty), +0000, -0400, +1030<br>https://www.journaldev.com/23365/python-string-to-datetime-strptime<br></td></tr></tbody></table>

 * ## Comparing timestamp and difference

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>#COMPARE TIME LIMIT FOR OTP<br>            import datetime<br>            import pytz<br>            #convert payload creation time to datetime<br>            creation_time = datetime.datetime.fromisoformat(payload['creation_time'])<br>            #datetime.timedelta(minutes=1, seconds=1)<br>            timelimit = datetime.timedelta(seconds=2)<br>            current_time = datetime.datetime.now(tz=pytz.timezone('UTC'))<br><br>            if current_time - creation_time &gt; timelimit:<br></td></tr></tbody></table>

 * ## How to store information of user\_login ip\_address, device, and multiple logins information

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>class UserSessionLog(models.Model):<br>    user = models.ForeignKey(settings.AUTH_USER_MODEL)<br>    device_type = models.CharField(max_length=255)<br>    ip_address = models.GenericIPAddressField()<br>    login_by_otp = models.BooleanField(default=False)<br>    login_by_pass = models.BooleanField(default=False)<br>    login_time = models.DateTimeField(auto_now=True)<br></td></tr></tbody></table>

 * ## How to get client ip address in Django

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>def get_client_ip(request):<br>    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')<br>    if x_forwarded_for:<br>        ip = x_forwarded_for.split(',')[0]<br>    else:<br>        ip = request.META.get('REMOTE_ADDR')<br>    return ip<br></td></tr></tbody></table>

 * ## Models on\_delete

     * https://stackoverflow.com/questions/38388423/what-does-on-delete-do-on-django-models

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>This is the behaviour to adopt when the referenced object is deleted. It is not specific to django, this is an SQL standard.<br><br>There are 6 possible actions to take when such event occurs:<br><br>CASCADE: When the referenced object is deleted, also delete the objects that have references to it (When you remove a blog post for instance, you might want to delete comments as well). SQL equivalent: CASCADE.<br>PROTECT: Forbid the deletion of the referenced object. To delete it you will have to delete all objects that reference it manually. SQL equivalent: RESTRICT.<br>SET_NULL: Set the reference to NULL (requires the field to be nullable). For instance, when you delete a User, you might want to keep the comments he posted on blog posts, but say it was posted by an anonymous (or deleted) user. SQL equivalent: SET NULL.<br>SET_DEFAULT: Set the default value. SQL equivalent: SET DEFAULT.<br>SET(...): Set a given value. This one is not part of the SQL standard and is entirely handled by Django.<br>DO_NOTHING: Probably a very bad idea since this would create integrity issues in your database (referencing an object that actually doesn't exist). SQL equivalent: NO ACTION.<br><br>In most cases, CASCADE is the expected behaviour, but for every ForeignKey, you should always ask yourself what is the expected behaviour in this situation. PROTECT and SET_NULL are often useful. Setting CASCADE where it should not, can potentially delete all your database in cascade, by simply deleting a single user.<br><br>"No! Please! Don't! I can't live without you!" (which is said PROTECT in SQL language)<br>"Alright, if I'm not yours, then I'm nobody's" (which is said SET_NULL)<br>"Good bye world, I can't live without article_B" and commit suicide (this is the CASCADE behavior).<br>"It's OK, I've got spare lover, I'll reference article_C from now" (SET_DEFAULT, or even SET(...)).<br>"I can't face reality, I'll keep calling your name even if that's the only thing left to me!" (DO_NOTHING)<br><br><br></td></tr></tbody></table>

 * ## Role of get\_user:

     * |                                                                                                                                                                                                                                          |

     * | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

     * | When you log in, Django stores the primary key of the user in the session. For each request, the authentication middleware calls get\_user() with this primary key, and sets request.user to the logged-in user. |

 * ## How the authentication works in Django

     * |                                                                                                                                                                                                                                                                                                                     |

     * | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

     * | In django before sending the response a session is created in the database. The session is stored in the database, not in the user's cookie. There is no way for the user to change that data. The only thing stored in the cookie is the hash of the session ID itself. |

     * Whenever a page is loaded in firefox/chrome it has a cookie called sessionid == (settings.SESSION\_COOKIE\_NAME)

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td># cookie<br>sessionid == (settings.SESSION_COOKIE_NAME)<br></td></tr></tbody></table>

     * Then to get the session\_key when a page is requested

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>#gauranga<br>session_key = request.COOKIES.get(settings.SESSION_COOKIE_NAME)<br></td></tr></tbody></table>

     * Then get the session back 

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>engine = import_module(settings.SESSION_ENGINE)<br>SessionStore = engine.SessionStore<br>request.session = SessionStore(session_key)<br></td></tr></tbody></table>

     * authenticate()

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>authenticate() will run the authenticate mehod of different backgrounds and returns a user object.<br><br>def authenticate(request=None, **credentials):<br>   For loop over all the authentication backends:<br>       # then mainly does the following things.<br>        user = backend.authenticate(request, **credentials)<br>        user.backend = backend_path<br>        return user<br><br>Example of backend:<br><br>class ModelBackend:<br>** for authenticate check the pass_word and also ****is_active . Else login will not check<br>    def authenticate(self, request, username=None, password=None, **kwargs):<br>            # it tries to get the user object from the user name<br>             user = UserModel._default_manager.get_by_natural_key(username)<br>             # then it checks the password and also is_active<br>             user.check_password(password) and self.user_can_authenticate(user):<br>             # then it returns the user<br>             return user<br></td></tr></tbody></table>

     * login()

     * After aunthenticating a user we add that information to the session using login.

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>login(request, user, banckend=None)<br>      1)     It will flush the current session (** in simplified terms. Check the code for more details)<br>                     --  _get_user_session_key(request) != user.pk<br>                     --  not constant_time_compare(request.session.get(HASH_SESSION_KEY, ''), session_auth_hash)) [*simplefied ### When password is changed https://docs.djangoproject.com/en/2.2/topics/auth/default/#session-invalidation-on-password-change<br>      2)     It will get the backend (either passed or set during authenticate by user.backend)<br>                        backend = backend or user.backend<br>      3)     It will set the following<br>                       request.session[SESSION_KEY] = user._meta.pk.value_to_string(user)<br>                       request.session[BACKEND_SESSION_KEY] = backend <br>                       # this sesstion_auth_hash = user.get_session_auth_hash() (this is generated using the SECRET_KEY and passwor. When we change password we want all the other sessions to logout. SO comparing this will do that)<br>                        request.session[HASH_SESSION_KEY] = session_auth_hash<br><ol start="4"><li> It will set request.user to the user passed</li></ol>             request.user is set by authentication middleware based on the request. But now in this  function we will set it to the user we want<br>                        request.user = user<br><ol start="5"><li> It will reset the csrf token</li></ol></td></tr></tbody></table>

     * What does AuthenticationMiddleware do:

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>It sets request.user using auth’s get_user<br>request.user = get_user(request) (** simplified way) (this will be a lazy object. Either it will be anonymous user or a User model<br><br>What auths get_user does:<br><br><ol><li>Gets the user_id and backend_path</li></ol>        user_id = _get_user_session_key(request)<br>        backend_path = request.session[BACKEND_SESSION_KEY]<br><br><ol start="2"><li> Get the user model instance for the corresponding user_id</li></ol>user = backend.get_user(user_id) [*** Here the get_user will check for active = True]<br><br>If (user has attr get_session_auth_hash) then it will check below<br><ol start="3"><li> Verify session w.r.t password change using get_session_auth_hash https://docs.djangoproject.com/en/2.2/topics/auth/default/#session-invalidation-on-password-change</li></ol><br>If not constant_time_compare(<br>                   request.session.get(HASH_SESSION_KEY) ,<br>                    user.get_session_auth_hash()<br>                )<br><br>Then<br>request.session.flush() and return<br> user is None. <br></td></tr></tbody></table>

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>AbstractBaseUser has a method called get_session_auth_hash<br><br>    def get_session_auth_hash(self):<br>        """<br>        Return an HMAC of the password field.<br>        """<br>        key_salt = "django.contrib.auth.models.AbstractBaseUser.get_session_auth_hash"<br>        return salted_hmac(key_salt, self.password).hexdigest()<br><br>And salted_hmac depends on settings.SECRET_KEY<br><br>Here we see that get_session_auth_hash: is used for password checking between sessions. And its mainly checked during login() and also get_user() in auth __init__<br><br>So its better to have a default password for security reasons.<br></td></tr></tbody></table>

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>user._meta.pk.value_to_string(user)   generates a session_key<br><br></td></tr></tbody></table>

 * ## Django model object.create vs object.save

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>create(**kwargs)<br>A convenience method for creating an object and saving it all in one step. Thus:<br><br>p = Person.objects.create(first_name="Bruce", last_name="Springsteen")<br>and:<br><br>p = Person(first_name="Bruce", last_name="Springsteen")<br>p.save(force_insert=True)<br>are equivalent.<br><br>The force_insert parameter is documented elsewhere, but all it means is that a new object will always be created. Normally you won’t need to worry about this. However, if your model contains a manual primary key value that you set and if that value already exists in the database, a call to create() will fail with an IntegrityError since primary keys must be unique. Be prepared to handle the exception if you are using manual primary keys.<br></td></tr></tbody></table>

 * ## Retrieving all field instances of a model

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>&gt;&gt;&gt; from django.contrib.auth.models import User<br>&gt;&gt;&gt; User._meta.get_fields()<br>(&lt;ManyToOneRel: admin.logentry&gt;,<br> &lt;django.db.models.fields.AutoField: id&gt;,<br> &lt;django.db.models.fields.CharField: password&gt;,<br> &lt;django.db.models.fields.DateTimeField: last_login&gt;,<br> &lt;django.db.models.fields.BooleanField: is_superuser&gt;,<br> &lt;django.db.models.fields.CharField: username&gt;,<br> &lt;django.db.models.fields.CharField: first_name&gt;,<br> &lt;django.db.models.fields.CharField: last_name&gt;,<br> &lt;django.db.models.fields.EmailField: email&gt;,<br> &lt;django.db.models.fields.BooleanField: is_staff&gt;,<br> &lt;django.db.models.fields.BooleanField: is_active&gt;,<br> &lt;django.db.models.fields.DateTimeField: date_joined&gt;,<br> &lt;django.db.models.fields.related.ManyToManyField: groups&gt;,<br> &lt;django.db.models.fields.related.ManyToManyField: user_permissions&gt;)<br><br># Also include hidden fields.<br>&gt;&gt;&gt; User._meta.get_fields(include_hidden=True)<br>(&lt;ManyToOneRel: auth.user_groups&gt;,<br> &lt;ManyToOneRel: auth.user_user_permissions&gt;,<br> &lt;ManyToOneRel: admin.logentry&gt;,<br> &lt;django.db.models.fields.AutoField: id&gt;,<br> &lt;django.db.models.fields.CharField: password&gt;,<br> &lt;django.db.models.fields.DateTimeField: last_login&gt;,<br> &lt;django.db.models.fields.BooleanField: is_superuser&gt;,<br> &lt;django.db.models.fields.CharField: username&gt;,<br> &lt;django.db.models.fields.CharField: first_name&gt;,<br> &lt;django.db.models.fields.CharField: last_name&gt;,<br> &lt;django.db.models.fields.EmailField: email&gt;,<br> &lt;django.db.models.fields.BooleanField: is_staff&gt;,<br> &lt;django.db.models.fields.BooleanField: is_active&gt;,<br> &lt;django.db.models.fields.DateTimeField: date_joined&gt;,<br> &lt;django.db.models.fields.related.ManyToManyField: groups&gt;,<br> &lt;django.db.models.fields.related.ManyToManyField: user_permissions&gt;)<br><br></td></tr></tbody></table>

 * ## Sort User dictionary for viewing

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>User_dict = User().__dict__<br>dict(sorted(User_dict.items(), key=lambda t: (str(t[1]), str(t[0])),reverse=True))<br></td></tr></tbody></table>

     * And for viewing all the properties

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>from basic_django import settings<br>for field in User._meta.fields:<br>    print(field.name)<br>    print(settings.pp_odir(field))<br></td></tr></tbody></table>

 * ## View all fields (including hidden) with only certain fields:

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>000_class<br>001_default<br>002_auto_created<br>003_auto_now_add<br>004_auto_now<br>005_null<br>006_empty_strings_allowed<br>007_blank<br>editable<br>hidden<br>mant_to_one<br>many_to_many<br>max_length<br>one_to_many<br>one_to_one<br>primary_key<br>related_model<br>remote_field<br>Unique<br><br>And after than it will check for <br>002_auto_created == True or <br>003_auto_now_add == True<br>004_auto_now = True<br>005_null = False and 001_default == ""<br>null = True<br>And remaining<br><br></td></tr></tbody></table>

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>all={}<br>from basic_django import settings<br>Model_meta = User._meta<br>for field in Model_meta.get_fields(include_hidden=True):<br>    all[field.name] = {}<br>    # store the __class__<br>    try: <br>        all[field.name]['000_class'] = settings.pp_odir_getobject(field)["00_METHODS********************************************************************************"]['__class__'] <br>    except KeyError:<br>        pass<br><br>    # store the default<br>    try: <br>        if Model_meta.get_field(field.name).get_default() is not None:<br>            all[field.name]['001_default'] = Model_meta.get_field(field.name).get_default()<br>    except:<br>        pass<br><br>    # store the null<br>    try: <br>        all[field.name]['005_null'] = settings.pp_odir_getobject(field)["02_OTHERS*********************************************************************************"]['null'] <br>    except KeyError:<br>        pass<br><br>    # store the blank<br>    try: <br>        all[field.name]['007_blank'] = settings.pp_odir_getobject(field)["02_OTHERS*********************************************************************************"]['blank'] <br>    except KeyError:<br>        pass<br><br>    # store the auto_now<br>    try: <br>        auto_now = settings.pp_odir_getobject(field)["02_OTHERS*********************************************************************************"]['auto_now'] <br>        if auto_now == True:<br>            all[field.name]['004_auto_now'] = auto_now<br>    except KeyError:<br>        pass<br><br><br>    # store the auto_now_add<br>    try: <br>        auto_now_add = settings.pp_odir_getobject(field)["02_OTHERS*********************************************************************************"]['auto_now_add'] <br>        if auto_now_add == True:<br>            all[field.name]['003_auto_now_add'] = auto_now_add<br>    except KeyError:<br>        pass<br><br><br>    # store the auto_created<br>    try: <br>        auto_created = settings.pp_odir_getobject(field)["02_OTHERS*********************************************************************************"]['auto_created'] <br>        if auto_created == True:<br>            all[field.name]['002_auto_created'] = auto_created<br>    except KeyError:<br>        pass<br><br>    # store the editable<br>    try: <br>        editable = settings.pp_odir_getobject(field)["02_OTHERS*********************************************************************************"]['editable'] <br>        if editable == False:<br>            all[field.name]['editable'] = editable<br>    except KeyError:<br>        pass<br><br><br>    # store the hidden<br>    try: <br>        hidden = settings.pp_odir_getobject(field)["02_OTHERS*********************************************************************************"]['hidden'] <br>        if hidden == True:<br>            all[field.name]['hidden'] = hidden<br>    except KeyError:<br>        pass<br><br><br>    # store the many_to_many<br>    try: <br>        many_to_many = settings.pp_odir_getobject(field)["02_OTHERS*********************************************************************************"]['many_to_many'] <br>        if many_to_many != None:<br>            all[field.name]['many_to_many'] = many_to_many<br>    except KeyError:<br>        pass<br><br><br>    # store the mant_to_one<br>    try: <br>        mant_to_one = settings.pp_odir_getobject(field)["02_OTHERS*********************************************************************************"]['mant_to_one'] <br>        if mant_to_one != None:<br>            all[field.name]['mant_to_one'] = mant_to_one<br>    except KeyError:<br>        pass<br><br><br>    # store the max_length<br>    try: <br>        max_length = settings.pp_odir_getobject(field)["02_OTHERS*********************************************************************************"]['max_length'] <br>        if max_length != None:<br>            all[field.name]['max_length'] = max_length<br>    except KeyError:<br>        pass<br><br><br>    # store the one_to_many<br>    try: <br>        one_to_many = settings.pp_odir_getobject(field)["02_OTHERS*********************************************************************************"]['one_to_many'] <br>        if one_to_many != None:<br>            all[field.name]['one_to_many'] = one_to_many<br>    except KeyError:<br>        pass<br><br><br>    # store the one_to_one<br>    try: <br>        one_to_one = settings.pp_odir_getobject(field)["02_OTHERS*********************************************************************************"]['one_to_one'] <br>        if one_to_one != None:<br>            all[field.name]['one_to_one'] = one_to_one<br>    except KeyError:<br>        pass<br><br>    # store the related_model<br>    try: <br>        related_model = settings.pp_odir_getobject(field)["02_OTHERS*********************************************************************************"]['related_model'] <br>        if related_model != None:<br>            all[field.name]['related_model'] = related_model<br>    except KeyError:<br>        pass<br><br>    # store the remote_field<br>    try: <br>        remote_field = settings.pp_odir_getobject(field)["02_OTHERS*********************************************************************************"]['remote_field'] <br>        if remote_field != None:<br>            all[field.name]['remote_field'] = remote_field<br>    except KeyError:<br>        pass<br><br><br>    # store the unique<br>    try: <br>        unique = settings.pp_odir_getobject(field)["02_OTHERS*********************************************************************************"]['unique'] <br>        if unique == True:<br>            all[field.name]['unique'] = unique<br>    except KeyError:<br>        pass<br><br>    # store the primary_key<br>    try: <br>        primary_key = settings.pp_odir_getobject(field)["02_OTHERS*********************************************************************************"]['primary_key'] <br>        if primary_key == True:<br>            all[field.name]['primary_key'] = primary_key<br>    except KeyError:<br>        pass<br><br>    # store the empty_strings_allowed<br>    try: <br>        empty_strings_allowed = settings.pp_odir_getobject(field)["02_OTHERS*********************************************************************************"]['empty_strings_allowed'] <br>        if empty_strings_allowed != None:<br>            all[field.name]['006_empty_strings_allowed'] = empty_strings_allowed<br>    except KeyError:<br>        pass<br><br>#print(settings.pp_odir(all))<br>c_dict = {<br>                "000_null_true***********************************************************************":{},<br>                '001_remaining***********************************************************************':{},<br>                "002_null_false_and_empty_strings****************************************************":{},                <br>                '003_auto_now_add__OR__auto_now******************************************************':{},<br>                "004_auto_created********************************************************************":{},<br>                "005_default_not_empty_string********************************************************":{},<br><br>                }<br><br>all2 = settings.keys_string(all)<br><br>for key, value in list(all2.items()):<br>    try:<br>        if all2[key]['003_auto_now_add'] == True:<br>            c_dict['003_auto_now_add__OR__auto_now******************************************************'][key] = all2[key]<br>            del all2[key]<br>    except:<br>        pass<br>    <br>    try:<br>        if all2[key]['004_auto_now'] == True:<br>            c_dict['003_auto_now_add__OR__auto_now******************************************************'][key] = all2[key]<br>            del all2[key]<br>    except:<br>        pass<br>    <br>    try:<br>        if all2[key]['002_auto_created'] == True:<br>            c_dict['004_auto_created********************************************************************'][key] = all2[key]<br>            del all2[key]<br>    except:<br>        pass<br><br>for key, value in list(all2.items()):<br>    try:<br>        if all2[key]['005_null'] == False:<br>            if all2[key]['001_default'] == '':<br>                c_dict['002_null_false_and_empty_strings****************************************************'][key] = all2[key]<br>                del all2[key]<br>    except:<br>        pass<br><br><br>for key, value in list(all2.items()):<br>    try:<br>        if all2[key]['001_default'] != '':<br>            c_dict['005_default_not_empty_string********************************************************'][key] = all2[key]<br>            del all2[key]<br>    except:<br>        pass<br><br>for key, value in list(all2.items()):        <br>    try:<br>        if all2[key]['005_null'] == True:<br>            c_dict['000_null_true***********************************************************************'][key] = all2[key]<br>            del all2[key]<br>    except:<br>        pass<br><br>for key, value in list(all2.items()):<br>    c_dict['001_remaining***********************************************************************'][key]= all2[key]<br><br>total_User_meta_hidden = len(Model_meta.get_fields(include_hidden=True))<br>print("total length of Model_meta.get_fields(include_hidden=True): ",total_User_meta_hidden )<br>print("\n")<br>print(settings.pp_odir(Model_meta.get_fields(include_hidden=True)))<br>print("\n")<br>print("Lenght of c_dict[000_null_true***********************************************************************] ",len(c_dict["000_null_true***********************************************************************"]))<br>print("Lenght of c_dict[001_remaining***********************************************************************] ",len(c_dict["001_remaining***********************************************************************"]))<br>print("Lenght of c_dict[002_null_false_and_empty_strings****************************************************] ",len(c_dict["002_null_false_and_empty_strings****************************************************"]))<br>print("Lenght of c_dict[003_auto_now_add__OR__auto_now******************************************************] ",len(c_dict["003_auto_now_add__OR__auto_now******************************************************"]))<br>print("Lenght of c_dict[004_auto_created********************************************************************] ",len(c_dict["004_auto_created********************************************************************"]))<br>print("Lenght of c_dict[005_default_not_empty_string********************************************************] ",len(c_dict["005_default_not_empty_string********************************************************"]))<br><br><br>total_c_dict = (<br>    len(c_dict["000_null_true***********************************************************************"])<br>    + len(c_dict["001_remaining***********************************************************************"])<br>    + len(c_dict["002_null_false_and_empty_strings****************************************************"])<br>    + len(c_dict["003_auto_now_add__OR__auto_now******************************************************"])<br>    + len(c_dict["004_auto_created********************************************************************"])<br>    + len(c_dict["005_default_not_empty_string********************************************************"])<br>    )<br><br>print("Total lenght of c_dict: ",total_c_dict)<br>print(settings.pp_odir(c_dict))<br></td></tr></tbody></table>

     * ### \[image\] run this script in jupyter

       * ![](images/image138.png)![](images/image187.png)![](images/image176.png)![](images/image220.png)![](images/image93.png)![](images/image55.png)![](images/image194.png)![](images/image99.png)![](images/image237.png)

     * ### \[image\] Output

       * ![](images/image1.png)![](images/image181.png)![](images/image100.png)![](images/image209.png)![](images/image73.png)![](images/image186.png)![](images/image29.png)![](images/image3.png)![](images/image144.png)![](images/image206.png)

 * ## auto\_now/auto\_now\_add will not update with .update

     * .update() will only update the fields explicitly passed to it, so datetimefields with auto\_now =True aren't updated.

     * Solution

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>from django.utils import timezone<br><br>class User(models.Model):<br>    created     = models.DateTimeField(editable=False)<br>    modified    = models.DateTimeField()<br><br>    def save(self, *args, **kwargs):<br>        ''' On save, update timestamps '''<br>        if not self.id:<br>            self.created = timezone.now()<br>        self.modified = timezone.now()<br>        return super(User, self).save(*args, **kwargs)<br></td></tr></tbody></table>

 * ## Django form editable

     * If False, the field will not be displayed in the admin or any other ModelForm. They are also skipped during model validation. Default is True.

     * This also happens with any field marked as auto\_now or auto\_now\_add, because that sets the editable=False on these fields.

 * ## Django set\_password and password validators and password changed

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>    #     You can also change a password programmatically, using set_password():<br>    # <br>    # &gt;&gt;&gt; from django.contrib.auth.models import User<br>    # &gt;&gt;&gt; u = User.objects.get(username='john')<br>    # &gt;&gt;&gt; u.set_password('new password')<br>    # &gt;&gt;&gt; u.save()<br></td></tr></tbody></table>

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>    # the following code is from copied as it is from /home/web_dev/django_basic_documentation/.venv/lib/python3.7/site-packages/django/contrib/auth/base_user.py<br>    # Stores the raw password if set_password() is called so that it can<br>    # be passed to password_changed() after the model is saved.<br>    _password = None<br><br>    from django.contrib.auth import password_validation<br>    #  the following code is copied as it is from /home/web_dev/django_basic_documentation/.venv/lib/python3.7/site-packages/django/contrib/auth/base_user.py<br>    def save(self, *args, **kwargs):<br>        super().save(*args, **kwargs)<br>        if self._password is not None:<br>            password_validation.password_changed(self._password, self)<br>            self._password = None<br><br>        # this note is for above code:<br>        # the purpose of password_changed is to <br><br></td></tr></tbody></table>

 * ## Specifying which fields to save by update\_fields rather than saving the whole fields again.

     * If save() is passed a list of field names in keyword argument update\_fields, only the fields named in that list will be updated. This may be desirable if you want to update just one or a few fields on an object. There will be a slight performance benefit from preventing all of the model fields from being updated in the database. For example:

     * product.name = 'Name changed again'

     * product.save(update\_fields=\['name'\])

     * The update\_fields argument can be any iterable containing strings. An empty update\_fields iterable will skip the save. A value of None will perform an update on all fields.

     * Specifying update\_fields will force an update.

 * ## How Django knows to UPDATE vs. INSERT¶

     * You may have noticed Django database objects use the same save() method for creating and changing objects. Django abstracts the need to use INSERT or UPDATE SQL statements. Specifically, when you call save(), Django follows this algorithm:

     * If the object’s primary key attribute is set to a value that evaluates to True (i.e., a value other than None or the empty string), Django executes an UPDATE.

     * If the object’s primary key attribute is not set or if the UPDATE didn’t update anything (e.g. if primary key is set to a value that doesn’t exist in the database), Django executes an INSERT.

 * ## Django Charfield null=False Integrity Error not raised

     * https://stackoverflow.com/questions/39176618/django-charfield-null-false-integrity-error-not-raised

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>If we try:<br>code = models.CharField(max_length=14, unique=True, null=False, blank=False)<br><br>model.save() will not raise any integrity error that code is not passed<br><br>Reason:<br></td></tr></tbody></table>

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td> default Django behavior will save CHAR or TEXT types as Null - it will always use an empty string (''). null=False has no effect on these types of fields.<br><br>And<br><br>blank=False means that the field will be required by default when the model is used to render a ModelForm. It does not prevent you from manually saving a model instance without that value.<br></td></tr></tbody></table>

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>What you want here is a custom model validator:<br><br>from django.core.exceptions import ValidationError<br>def validate_not_empty(value):<br>    if value == '':<br>        raise ValidationError('%(value)s is empty!'), params={'value':value})<br><br>Then add the validator to your model:<br><br>code = models.CharField(max_length=14, unique=True, validators=[validate_not_empty])<br><br>This will take care of the form validation you want, but validators don't automatically run when a model instance is saved. <br><br>Further reading here. If you want to validate this every time an instance is saved, I suggest overriding the default save behavior, checking the value of your string there, and interrupting the save by raising an error if necessary. <br><br>Good post on overriding save here.<br><br></td></tr></tbody></table>

 * ## Raise a validation error in a model's save method in Django

     * [https://stackoverflow.com/a/8771090/2897115](https://www.google.com/url?q=https://stackoverflow.com/a/8771090/2897115&sa=D&ust=1571383145587000)

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>Most Django views e.g. the Django admin will not be able to handle a validation error in the save method, so your users will get 500 errors.<br><br>You should do validation on the model form or on the model, and raise ValidationError there. Then call save() only if the model form data is 'good enough to save'.<br></td></tr></tbody></table>

     * https://stackoverflow.com/a/52949929/2897115

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>But in general, it's not good practice to add validation in the save() method. The reason is that in most Django apps, you'd create a form (a ModelForm) which would call the validation methods and be able to return something meaningful to the user when validation fails.<br><br>When the model's save() method is called it's too late to show something to the user, so you can only raise an exception at that point (and crash).<br><br>The normal procedure (which the admin forms use) is: validate the form by calling form.is_valid() (which calls full_clean() on the model), then if and only if the form is valid, save the model.<br><br>The shell is not the regular interaction method and should be used only very carefully as it bypasses the normal flow of the application.<br></td></tr></tbody></table>

 * ## Difference between super() and super (className,self) in Python \[duplicate\]

     * In Python 2, only the super(className,self) syntax was possible. Since It was the most used version, as of Python 3 providing no arguments will act the same.

 * ## Sublime Text expand Selection to indentation

     * { "keys": \["ctrl+shift+j"\], "command": "expand\_selection", "args": {"to": "indentation"} },

 * ## Sublime Text folding

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>        { "keys": ["ctrl+shift+["], "command": "fold" },<br>        { "keys": ["ctrl+shift+]"], "command": "unfold" },<br>        { "keys": ["ctrl+k", "ctrl+1"], "command": "fold_by_level", "args": {"level": 1} },<br>        { "keys": ["ctrl+k", "ctrl+2"], "command": "fold_by_level", "args": {"level": 2} },<br>        { "keys": ["ctrl+k", "ctrl+3"], "command": "fold_by_level", "args": {"level": 3} },<br>        { "keys": ["ctrl+k", "ctrl+4"], "command": "fold_by_level", "args": {"level": 4} },<br>        { "keys": ["ctrl+k", "ctrl+5"], "command": "fold_by_level", "args": {"level": 5} },<br>        { "keys": ["ctrl+k", "ctrl+6"], "command": "fold_by_level", "args": {"level": 6} },<br>        { "keys": ["ctrl+k", "ctrl+7"], "command": "fold_by_level", "args": {"level": 7} },<br>        { "keys": ["ctrl+k", "ctrl+8"], "command": "fold_by_level", "args": {"level": 8} },<br>        { "keys": ["ctrl+k", "ctrl+9"], "command": "fold_by_level", "args": {"level": 9} },<br>        { "keys": ["ctrl+k", "ctrl+0"], "command": "unfold_all" },<br>        { "keys": ["ctrl+k", "ctrl+j"], "command": "unfold_all" },<br>        { "keys": ["ctrl+k", "ctrl+t"], "command": "fold_tag_attributes" },<br></td></tr></tbody></table>

 * ## User.save(update\_fields=\[‘last\_login’\])

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>def update_last_login(sender, user, **kwargs):<br>    """<br>    A signal receiver which updates the last_login date for<br>    the user logging in.<br>    """<br>    user.last_login = timezone.now()<br>    user.save(update_fields=['last_login'])<br></td></tr></tbody></table>

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>Specifying which fields to save¶<br>If save() is passed a list of field names in keyword argument update_fields, only the fields named in that list will be updated. This may be desirable if you want to update just one or a few fields on an object. There will be a slight performance benefit from preventing all of the model fields from being updated in the database. For example:<br><br>product.name = 'Name changed again'<br>product.save(update_fields=['name'])<br>The update_fields argument can be any iterable containing strings. An empty update_fields iterable will skip the save. A value of None will perform an update on all fields.<br><br>Specifying update_fields will force an update.<br></td></tr></tbody></table>

     * Django signals:

     * |                                                                                                                                                                                                               |

     * | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

     * | signals allow certain senders to notify a set of receivers that some action has taken place. They’re especially useful when many pieces of code may be interested in the same events. |

     * Create signals

     * We create our custom signals by creating a signals.py file in our jobs\_board\_main application:

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td># jobs_board_main/signals.py<br>from django.dispatch import Signal<br><br>new_subscriber = Signal(providing_args=["job", "subscriber"])<br></td></tr></tbody></table>

     * That's it\! Our custom signal is ready to be invoked after a user has successfully subscribed to a job posting as follows in our jobs\_board\_main/views.py file:

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td># jobs_board_main/views.py<br><br># Existing imports and code are maintained and truncated for brevity<br>from .signals import new_subscriber<br><br>def subscribe(request, id):<br>    job = Job.objects.get(pk=id)<br>    subscriber = Subscriber(email=request.POST['email'])<br>    subscriber.save()<br><br>    subscription = Subscription(user=subscriber, job=job, email=subscriber.email)<br>    subscription.save()<br><br>    # Add this line that sends our custom signal<br>    new_subscriber.send(sender=subscription, job=job, subscriber=subscriber)<br><br>    payload = {<br>      'job': job,<br>      'email': request.POST['email']<br>    }<br>    return render(request, 'subscribed.html', {'payload': payload})<br><br></td></tr></tbody></table>

     * Note:A sender must either be a Python object, or None to receive events from any sender.

     * Let us now consume the signals that we have just sent in a separate jobs\_board\_notifications app.

     * Let us receive our signals in our jobs\_board\_notifications/models.py:

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td># jobs_board_notifications/models.py.<br>from django.db.models.signals import pre_delete<br>from django.dispatch import receiver<br><br>from jobs_board_main.signals import new_subscriber<br>from jobs_board_main.models import Job, Subscriber, Subscription<br><br>@receiver(new_subscriber, sender=Subscription)<br>def handle_new_subscription(sender, **kwargs):<br>    subscriber = kwargs['subscriber']<br>    job = kwargs['job']<br><br>    message = """User {} has just subscribed to the Job {}.<br>    """.format(subscriber.email, job.title)<br><br>    print(message)<br></td></tr></tbody></table>

 * ## Delete a object

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>from basic_django import settings<br>import logging<br>logger_database = logging.getLogger("django.db.backends")<br>logger_database.filters[0].open()<br>from custom_user.models import User<br>#User.objects.get(email='somename@gmail.com').delete()<br>instance = User.objects.filter(email='somename@gmail.com')<br>hare = instance.delete()<br>print(settings.pp_odir(hare))<br>logger_database.filters[0].close()<br></td></tr></tbody></table>

 * ## logout() and maximum recursion depth exceeded on logout(request)

     * \# never use the same name as logout(request) it will cause recurssion error

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>def logout_view(request):<br>    # never use the same name as logout(request) it will cause recurssion error<br>    email = request.user.email<br>    logout(request)<br><br>    ## CLEARING ALL THE MESSAGES<br>    system_messages = messages.get_messages(request)<br>    for message in system_messages:<br>        # This iteration is necessary<br>        pass<br>    system_messages.used = True<br><br>    messages.success(request, email,' has logged out successfully')<br>    return redirect('articles_namespace:articles')<br></td></tr></tbody></table>

 * ## Model.objects.get() (should return only one object)

     * get()¶

     * get(\*\*kwargs)¶

     * Returns the object matching the given lookup parameters, which should be in the format described in Field lookups.

     * get() raises MultipleObjectsReturned if more than one object was found. The MultipleObjectsReturned exception is an attribute of the model class.

     * get() raises a DoesNotExist exception if an object wasn’t found for the given parameters. This exception is an attribute of the model class. Example:

 * ## Git insert commit inbetween

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>git rebase -i &lt;any earlier commit&gt;. This displays a list of commits in your configured text editor.<br><br>Find the commit you want to insert after (let's assume it's a1b2c3d). In your editor, for that line, change pick to edit.<br><br>Begin the rebase by closing your text editor (save your changes). This leaves you at a command prompt with the commit you chose earlier (a1b2c3d) as if it has just been committed.<br><br>Make your changes and git commit (NOT amending, unlike most edits). This creates new a commit after the one you chose.<br><br>git rebase --continue. This replays the successive commits, leaving your new commit inserted in the correct place.<br><br>Beware that this will rewrite history, and break anyone else who tries to pull.<br></td></tr></tbody></table>

     * GIt checkout old commit and come back again

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>To return to your 'latest' commit checkout the branch you were working on. Either<br><br>git checkout master<br><br>or any other branch<br><br>git checkout &lt;my_branch&gt;<br><br>Checking previous commit or any commit which is not in a branch gets you in Detached HEAD state. This is valid state in git. Your working directory is updated and you can develop. What you cannot do in this state is perform commits. If you want to continue developing from some historical you can branch out from there. Example:<br><br>git checkout &lt;some_hash_in_the_past&gt;<br>... Detached head<br>git branch &lt;my_new_branch&gt;<br>... edit files<br>git add/commit<br><br><br>The most useful thing you can do with it is explore an older state of a repository. Afterwards, you’ll probably want to return to the branch you came from. You can do this with git checkout -. Interesting tidbit about the dash: it’s a shortcut for “the branch or commit you were on before your last checkout command.<br></td></tr></tbody></table>

 * ## How to revert initial git commit?

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>You just need to delete the branch you are on. You can't use git branch -D as this has a safety check against doing this. You can use update-ref to do this.<br><br>git update-ref -d HEAD<br></td></tr></tbody></table>

 * ## Recursively removes all .pyc files and \_\_pycache\_\_ directories in the current directory

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>#!/bin/sh<br><br># recursively removes all .pyc files and __pycache__ directories in the current<br># directory<br><br>find . | \<br>  grep -E "(__pycache__|\.pyc$)" | \<br>  xargs rm -rf<br><br># or, for copy-pasting:<br># find . | grep -E "(__pycache__|\.pyc$)" | xargs rm -rf<br><br></td></tr></tbody></table>

 * ## Git how to revert back to the last commit by cleaning the working directory

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>git reset --hard &amp;&amp; git clean -df<br><br>[ reset --hard ] will not remove untracked files so we have to do <br><br>[ git clean -df ] (which will remove untracked files and directories also) if use [ -x ] then it will remove ignored files also.<br><br>Also before doing [ git clean -df ] if we want to check we can do<br><br>[ git clean -n -dfx ]  (will show what all untracked files will be deleted including ignored files)<br><br>[ git clean -n -df ]  (will show what all untracked files will be deleted without ignored files)<br></td></tr></tbody></table>

 * ## Git ammed without opening the editor

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>#gauranga<br>git commit --amend --no-edit<br><br>If one short to amend and push<br>git add -A &amp;&amp; git commit --amend --no-edit &amp;&amp; git push -f --all origin<br></td></tr></tbody></table>

 * ## ffmpeg : how to record a gif:

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>In linux install SimpleScreenRecorder<br><br>Select the rectangular region and then save the screencast. Use mp4<br><br>Then conver the mp4 to gif using<br><br> ffmpeg -i input.mp4 -vf "fps=10,scale=320:-1:flags=lanczos" -c:v pam -f image2pipe - | convert -delay 10 - -loop 0 -layers optimize output.gif<br></td></tr></tbody></table>

 * ## Git how to use rebase --onto

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>Intially we have<br><br>1 -- 2 -- 3 -- 4 -- 5 -- 6  (master)<br>                    \<br>                     \ - 7--8 (testing)<br><br>When we do a rebase on master (git rebase -i --root ) And change the commit 1 then it becomes the following Because rebase will create a new copy of the master<br><br>1’ -- 2’ -- 3’ -- 4’ -- 5’ -- 6’  ((new) master branch)<br><br>4--7--8 (testing branch)<br><br>Now to combine the testing branch back to the new master branch we do OR<br>Transplant testing to the new history<br><br>git rebase --onto e507db5 (commit 4’) 9ad7f9a (commit 4) testing<br><br><a href="https://www.google.com/url?q=https://tag1consulting.com/blog/git-rebase-simple-one-minute-explanation&amp;sa=D&amp;ust=1571383145634000" class="c24">https://tag1consulting.com/blog/git-rebase-simple-one-minute-explanation</a><br><br>git rebase --onto [the new HEAD base] [the old head base - check git log] [the-branch-to-rebase-from-one-base-to-another]<br><br>You have:<br>Two red dishes on top of two blue dishes<br>One yellow dish<br><br>You want:<br>Those two red dishes on top of the one yellow dish<br><br>You do:<br>Carefully go with the finger down to the bottom of the two red dishes, which is the first blue dish<br>Take the two red dishes<br>Transfer them over to the one yellow dish<br><br>That is what rebase --onto does:<br><br>git rebase --onto [yellow dish] [from: first blue dish] [the two red dishes]<br><br>******* Deleting commits<br><br>Here's an example:<br><br>o---A---X---Y---Z master<br><br>To remove the last 3 commits X, Y and Z, you just need:<br><br>git rebase --onto A Z<br><br>*********<br></td></tr></tbody></table>

     * ### Git rebase (two argument form)

       * ![](images/image53.png)

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>I like to think about git rebase --onto/2 git rebase "where I want to go" from "where I was"<br><br>"where I want to go" being the object identifier of the place you want all your commits to go to<br><br>"where I was" to be the object identifier of where your branch is currently sitting off at.<br><br>git rebase --onto (has of commit D) (hash of commit C)<br></td></tr></tbody></table>

     * ### Git rebase (another explanation)

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>              A---B---C topic<br>             /<br>    D---E---F---G master<br></td></tr></tbody></table>

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>From this point, the result of either of the following commands:<br><br>git rebase master<br>git rebase master topic  (git checkout topic followed by git rebase master)<br><br>                          A'--B'--C' topic<br>                         /<br>    D---E---F---G master<br><br></td></tr></tbody></table>

 * ## Insert a commit before the root commit in Git?

     * [https://stackoverflow.com/questions/645450/insert-a-commit-before-the-root-commit-in-git](https://www.google.com/url?q=https://stackoverflow.com/questions/645450/insert-a-commit-before-the-root-commit-in-git&sa=D&ust=1571383145647000)

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>First create an empty commit. This will be added to the lastest commit<br><br>git commit --allow-empty -m 'ZERO COMMIT Documentation related'<br><br>Second, switch the order of the commits using:<br><br>git rebase -i --root<br><br>An editor will appear with the commits until the root commit, like:<br><br>pick 1234 old root message<br><br>pick 0294 A commit in the middle<br><br>pick 5678 commit you want to put at the root<br><br>You can then put the commit you want first, by placing it in the first line. In the example:<br><br>pick 5678 commit you want to put at the root<br><br>pick 1234 old root message<br><br>pick 0294 A commit in the middle<br><br>Exit the editor the commit order will have changed.<br><br></td></tr></tbody></table>

 * ## Ammed the latest git commit message if its empty git

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>If i have created an empty git<br><br>git commit --allow-empty -m 'ZERO COMMIT Documentation related' <br><br>and not we want to change the message then do<br><br>git commit --allow-empty --amend (it will open the editor, do the changes and save)<br></td></tr></tbody></table>

 * ## How to make Git “forget” about a file that was tracked but is now in .gitignore?

     * [http://www.codeblocq.com/2016/01/Untrack-files-already-added-to-git-repository-based-on-gitignore/](https://www.google.com/url?q=http://www.codeblocq.com/2016/01/Untrack-files-already-added-to-git-repository-based-on-gitignore/&sa=D&ust=1571383145654000)

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>.gitignore will prevent untracked files from being added (without an add -f) to the set of files tracked by git, <br><br>however git will continue to track any files that are already being tracked.<br><br>To stop tracking a file you need to remove it from the index. This can be achieved with this command.<br><br>**********<br>git rm --cached &lt;file&gt;<br>**********<br>If you want to remove a whole folder, you need to remove all files in it recursively.<br><br>**********<br>git rm -r --cached &lt;folder&gt;<br><br>-r means recursively. Better go to the root directory and do [ rm -r --cached . ]<br>-- cached : will only remove files from the index. Your files will still be there.<br>**********<br><br>The removal of the file from the head revision will happen on the next commit.<br><br>WARNING: While this will not remove the physical file from your local, it will remove the files from other developers machines on next git pull.<br><br>IF WE WANT TO REMOVE THE FILE FROM PAST ALSO:<br><br>Then find the file’s first commit and go into it using rebase and then <br><br>git rm --cached that file; then<br><br>Git add -A<br><br>Then <br><br>git rebase --continue<br></td></tr></tbody></table>

 * ## How to insert a commit inbetween

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td><br>Create an empty commit<br><br>git commit --allow-empty -m 'ZERO COMMIT Documentation related' <br><br>Then do rebase and in the editor move it up or down and saves<br></td></tr></tbody></table>

