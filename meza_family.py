from pywikibot import family

class Family(family.Family):
	name = "meza"
	langs = {
		"en": None
	}
	
	def hostname(self, code):
		return "192.168.56.56"

	def scriptpath(self, code):
		return "/demo"

	def protocol(self, code):
		return "HTTPS"

	def ignore_certificate_error(self, code):
		return True

