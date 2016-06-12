from suggestionsapp import nav_urls

def navbar(request):
	return {
		'nav_urls': nav_urls.navurlpatterns,
	}