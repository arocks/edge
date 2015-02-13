# deployment
env=development

configure:
	@ansible-playbook devops/start.yml -i devops/inventory/$(env) --limit=all

deploy:
	@ansible-playbook devops/launch.yml -i devops/inventory/$(env) --limit=all -vvvvvvv

# for dev debugging.
run2:
	@sudo killall -9 supervisord | echo 
	@sudo killall -9 gunicorn | echo
	@python manage.py validate --settings=settings.development &
	@python manage.py collectstatic --noinput --settings=settings.development &
	@python manage.py migrate --settings=settings.development &
	@python manage.py runserver 0.0.0.0:8000 --settings=settings.development

shell:
	@python manage.py shell_plus --settings=settings.development