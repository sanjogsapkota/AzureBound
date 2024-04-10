class Boton():
	def __init__(self, imagen, pos, texto_entrada, fuente, color_base, color_flotante):
		self.imagen = imagen
		self.x_pos = pos[0]
		self.y_pos = pos[1]
		self.fuente = fuente
		self.color_base, self.color_flotante = color_base, color_flotante
		self.entrada_texto = texto_entrada
		self.texto = self.fuente.render(self.entrada_texto, True, self.color_base)
		if self.imagen is None:
			self.imagen = self.texto
		self.rect = self.imagen.get_rect(center=(self.x_pos, self.y_pos))
		self.texto_rect = self.texto.get_rect(center=(self.x_pos, self.y_pos))

	def actualizar(self, pantalla):
		if self.imagen is not None:
			pantalla.blit(self.imagen, self.rect)
		pantalla.blit(self.texto, self.texto_rect)

	def verificar_entrada(self, posicion):
		if posicion[0] in range(self.rect.left, self.rect.right) and posicion[1] in range(self.rect.top, self.rect.bottom):
			return True
		return False

	def cambiar_color(self, posicion):
		if posicion[0] in range(self.rect.left, self.rect.right) and posicion[1] in range(self.rect.top, self.rect.bottom):
			self.texto = self.fuente.render(self.entrada_texto, True, self.color_flotante)
		else:
			self.texto = self.fuente.render(self.entrada_texto, True, self.color_base)