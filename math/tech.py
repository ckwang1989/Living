	def get_KD(highes, lowes, closes, nKD=9):
		'''
		function: KD
			input:

			output:

		'''
		K_old, D_old = 0.0, 0.0
		Ks, Ds = [], []
		highes_tmp, lowes_tmp = [], []
		for i in range(0, len(highes)):
			highes_tmp.append(highes[i])
			lowes_tmp.append(lowes[i])
			if i >= nKD-1:
				lower = min(lowes_tmp)
				higher = max(highes_tmp)
				close = closes[i]
				
				RSV = 100.0 * ((close-lower)/(higher-lower+0.00000001))
				K_new = (2 * K_old / 3) + (RSV / 3)
				D_new = (2 * D_old / 3) + (K_new / 3)
				K_old, D_old = K_new, D_new
				highes_tmp.pop(0)
				lowes_tmp.pop(0)
			Ks.append(K_old)
			Ds.append(D_old)

		return Ks, Ds