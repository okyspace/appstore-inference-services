def load_model(filepath):
	return filepath

def load_others(filepath):
	return ""

def read_data(filepath):
	return filepath

def infer(model, data, device):
	return data

def main():
	model = load_model()
	data = read_data()
	result = infer(model, data)
	return result

if __name__ == '__main__':
	main()
