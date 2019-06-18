#
# Prepare openapi files and run projects in containers.
#
YAML=$(shell find * -name \*yaml)
YAMLSRC=$(shell find openapi -name \*yaml.src)
YAMLGEN=$(patsubst %.yaml.src,%.yaml,$(YAMLSRC))

yaml: $(YAMLGEN)

.ONESHELL:
%.yaml: %.yaml.src
	tox -e yamllint -- -d relaxed $<
	tox -e yaml 2>/dev/null --  $< $@ 

yamllint: $(YAML)
	tox -e yamllint -- $<

java-jaxrs-generate: openapi/simple.yaml
	./scripts/codegen.sh openapi/simple.yaml java-jaxrs 3 jaxrs-resteasy-eap

java-jaxrs-quickstart: java-jaxrs-generate
	(cd java-jaxrs && docker-compose up simple )
	
