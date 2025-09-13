from flask import Flask, render_template, request

app = Flask(__name__)

# Расширенные данные о комплектующих
components_data = {
    'gpu': {
        'NVIDIA RTX 4090': {'brand': 'NVIDIA', 'model': 'RTX 4090', 'vram': 24, 'memory_type': 'GDDR6X', 'bus_width': 384, 'price': 200000, 'rating': 5, 'release_year': 2022},
        'NVIDIA RTX 4080': {'brand': 'NVIDIA', 'model': 'RTX 4080', 'vram': 16, 'memory_type': 'GDDR6X', 'bus_width': 256, 'price': 120000, 'rating': 4, 'release_year': 2022},
        'NVIDIA RTX 4070 Ti': {'brand': 'NVIDIA', 'model': 'RTX 4070 Ti', 'vram': 12, 'memory_type': 'GDDR6X', 'bus_width': 192, 'price': 90000, 'rating': 4, 'release_year': 2023},
        'NVIDIA RTX 4070': {'brand': 'NVIDIA', 'model': 'RTX 4070', 'vram': 12, 'memory_type': 'GDDR6X', 'bus_width': 192, 'price': 80000, 'rating': 4, 'release_year': 2023},
        'NVIDIA RTX 4060 Ti': {'brand': 'NVIDIA', 'model': 'RTX 4060 Ti', 'vram': 8, 'memory_type': 'GDDR6', 'bus_width': 128, 'price': 50000, 'rating': 3, 'release_year': 2023},
        'NVIDIA RTX 4060': {'brand': 'NVIDIA', 'model': 'RTX 4060', 'vram': 8, 'memory_type': 'GDDR6', 'bus_width': 128, 'price': 40000, 'rating': 3, 'release_year': 2023},
        'NVIDIA RTX 3090 Ti': {'brand': 'NVIDIA', 'model': 'RTX 3090 Ti', 'vram': 24, 'memory_type': 'GDDR6X', 'bus_width': 384, 'price': 180000, 'rating': 5, 'release_year': 2022},
        'NVIDIA RTX 3080 Ti': {'brand': 'NVIDIA', 'model': 'RTX 3080 Ti', 'vram': 12, 'memory_type': 'GDDR6X', 'bus_width': 384, 'price': 110000, 'rating': 4, 'release_year': 2021},
        'AMD RX 7900 XTX': {'brand': 'AMD', 'model': 'RX 7900 XTX', 'vram': 24, 'memory_type': 'GDDR6', 'bus_width': 384, 'price': 110000, 'rating': 4, 'release_year': 2022},
        'AMD RX 7900 XT': {'brand': 'AMD', 'model': 'RX 7900 XT', 'vram': 20, 'memory_type': 'GDDR6', 'bus_width': 320, 'price': 95000, 'rating': 4, 'release_year': 2022},
        'AMD RX 7800 XT': {'brand': 'AMD', 'model': 'RX 7800 XT', 'vram': 16, 'memory_type': 'GDDR6', 'bus_width': 256, 'price': 70000, 'rating': 4, 'release_year': 2023},
        'AMD RX 7700 XT': {'brand': 'AMD', 'model': 'RX 7700 XT', 'vram': 12, 'memory_type': 'GDDR6', 'bus_width': 192, 'price': 55000, 'rating': 3, 'release_year': 2023},
        'AMD RX 7600': {'brand': 'AMD', 'model': 'RX 7600', 'vram': 8, 'memory_type': 'GDDR6', 'bus_width': 128, 'price': 35000, 'rating': 3, 'release_year': 2023},
    },
    'cpu': {
        'Intel Core i9-13900K': {'brand': 'Intel', 'model': 'Core i9-13900K', 'cores': 24, 'threads': 32, 'frequency': 5.8, 'socket': 'LGA1700', 'price': 60000, 'rating': 5, 'release_year': 2022},
        'Intel Core i7-13700K': {'brand': 'Intel', 'model': 'Core i7-13700K', 'cores': 16, 'threads': 24, 'frequency': 5.4, 'socket': 'LGA1700', 'price': 45000, 'rating': 4, 'release_year': 2022},
        'Intel Core i5-13600K': {'brand': 'Intel', 'model': 'Core i5-13600K', 'cores': 14, 'threads': 20, 'frequency': 5.1, 'socket': 'LGA1700', 'price': 32000, 'rating': 4, 'release_year': 2022},
        'Intel Core i9-12900K': {'brand': 'Intel', 'model': 'Core i9-12900K', 'cores': 16, 'threads': 24, 'frequency': 5.2, 'socket': 'LGA1700', 'price': 50000, 'rating': 4, 'release_year': 2021},
        'Intel Core i7-12700K': {'brand': 'Intel', 'model': 'Core i7-12700K', 'cores': 12, 'threads': 20, 'frequency': 5.0, 'socket': 'LGA1700', 'price': 38000, 'rating': 4, 'release_year': 2021},
        'Intel Xeon W-3375': {'brand': 'Intel', 'model': 'Xeon W-3375', 'cores': 38, 'threads': 76, 'frequency': 4.0, 'socket': 'LGA4189', 'price': 450000, 'rating': 5, 'release_year': 2021},
        'AMD Ryzen 9 7950X': {'brand': 'AMD', 'model': 'Ryzen 9 7950X', 'cores': 16, 'threads': 32, 'frequency': 5.7, 'socket': 'AM5', 'price': 65000, 'rating': 5, 'release_year': 2022},
        'AMD Ryzen 9 7900X': {'brand': 'AMD', 'model': 'Ryzen 9 7900X', 'cores': 12, 'threads': 24, 'frequency': 5.6, 'socket': 'AM5', 'price': 50000, 'rating': 4, 'release_year': 2022},
        'AMD Ryzen 7 7800X3D': {'brand': 'AMD', 'model': 'Ryzen 7 7800X3D', 'cores': 8, 'threads': 16, 'frequency': 5.0, 'socket': 'AM5', 'price': 40000, 'rating': 4, 'release_year': 2023},
        'AMD Ryzen 7 7700X': {'brand': 'AMD', 'model': 'Ryzen 7 7700X', 'cores': 8, 'threads': 16, 'frequency': 5.4, 'socket': 'AM5', 'price': 35000, 'rating': 4, 'release_year': 2022},
        'AMD Ryzen 5 7600X': {'brand': 'AMD', 'model': 'Ryzen 5 7600X', 'cores': 6, 'threads': 12, 'frequency': 5.3, 'socket': 'AM5', 'price': 28000, 'rating': 4, 'release_year': 2022},
        'AMD Ryzen 9 5950X': {'brand': 'AMD', 'model': 'Ryzen 9 5950X', 'cores': 16, 'threads': 32, 'frequency': 4.9, 'socket': 'AM4', 'price': 55000, 'rating': 5, 'release_year': 2020},
        'AMD Threadripper 3990X': {'brand': 'AMD', 'model': 'Threadripper 3990X', 'cores': 64, 'threads': 128, 'frequency': 4.3, 'socket': 'sTRX4', 'price': 350000, 'rating': 5, 'release_year': 2020},
        'AMD EPYC 9654': {'brand': 'AMD', 'model': 'EPYC 9654', 'cores': 96, 'threads': 192, 'frequency': 3.7, 'socket': 'SP5', 'price': 850000, 'rating': 5, 'release_year': 2022},
    },
    'ram': {
        'G.Skill Trident Z5 RGB 32GB': {'brand': 'G.Skill', 'model': 'Trident Z5 RGB', 'size': 32, 'type': 'DDR5', 'frequency': 6000, 'timing': 'CL36', 'price': 15000, 'rating': 5, 'release_year': 2022},
        'G.Skill Trident Z5 RGB 16GB': {'brand': 'G.Skill', 'model': 'Trident Z5 RGB', 'size': 16, 'type': 'DDR5', 'frequency': 6000, 'timing': 'CL36', 'price': 8000, 'rating': 4, 'release_year': 2022},
        'Kingston Fury Beast 32GB': {'brand': 'Kingston', 'model': 'Fury Beast', 'size': 32, 'type': 'DDR5', 'frequency': 5600, 'timing': 'CL40', 'price': 12000, 'rating': 4, 'release_year': 2022},
        'Kingston Fury Beast 16GB': {'brand': 'Kingston', 'model': 'Fury Beast', 'size': 16, 'type': 'DDR5', 'frequency': 5600, 'timing': 'CL40', 'price': 6000, 'rating': 4, 'release_year': 2022},
        'Teamgroup T-Force Delta 32GB': {'brand': 'Teamgroup', 'model': 'T-Force Delta', 'size': 32, 'type': 'DDR5', 'frequency': 6000, 'timing': 'CL38', 'price': 11000, 'rating': 4, 'release_year': 2022},
        'Teamgroup T-Force Delta 16GB': {'brand': 'Teamgroup', 'model': 'T-Force Delta', 'size': 16, 'type': 'DDR5', 'frequency': 6000, 'timing': 'CL38', 'price': 5500, 'rating': 4, 'release_year': 2022},
        'ADATA XPG Lancer 32GB': {'brand': 'ADATA', 'model': 'XPG Lancer', 'size': 32, 'type': 'DDR5', 'frequency': 5200, 'timing': 'CL38', 'price': 13000, 'rating': 4, 'release_year': 2022},
        'ADATA XPG Lancer 16GB': {'brand': 'ADATA', 'model': 'XPG Lancer', 'size': 16, 'type': 'DDR5', 'frequency': 5200, 'timing': 'CL38', 'price': 6500, 'rating': 4, 'release_year': 2022},
        'G.Skill Trident Z Neo 32GB': {'brand': 'G.Skill', 'model': 'Trident Z Neo', 'size': 32, 'type': 'DDR4', 'frequency': 3600, 'timing': 'CL16', 'price': 10000, 'rating': 5, 'release_year': 2020},
        'Kingston Fury Renegade 32GB': {'brand': 'Kingston', 'model': 'Fury Renegade', 'size': 32, 'type': 'DDR4', 'frequency': 3600, 'timing': 'CL16', 'price': 9000, 'rating': 4, 'release_year': 2021},
    },
    'motherboard': {
        'ASUS ROG Maximus Z790 Hero': {'brand': 'ASUS', 'model': 'ROG Maximus Z790 Hero', 'socket': 'LGA1700', 'chipset': 'Z790', 'memory_type': 'DDR5', 'price': 55000, 'rating': 5, 'release_year': 2022},
        'Gigabyte Z790 AORUS Master': {'brand': 'Gigabyte', 'model': 'Z790 AORUS Master', 'socket': 'LGA1700', 'chipset': 'Z790', 'memory_type': 'DDR5', 'price': 45000, 'rating': 5, 'release_year': 2022},
        'MSI MPG Z790 Carbon WiFi': {'brand': 'MSI', 'model': 'MPG Z790 Carbon WiFi', 'socket': 'LGA1700', 'chipset': 'Z790', 'memory_type': 'DDR5', 'price': 40000, 'rating': 4, 'release_year': 2022},
        'ASRock Z790 Taichi': {'brand': 'ASRock', 'model': 'Z790 Taichi', 'socket': 'LGA1700', 'chipset': 'Z790', 'memory_type': 'DDR5', 'price': 42000, 'rating': 4, 'release_year': 2022},
        'ASUS ROG Strix X670E-E Gaming': {'brand': 'ASUS', 'model': 'ROG Strix X670E-E Gaming', 'socket': 'AM5', 'chipset': 'X670E', 'memory_type': 'DDR5', 'price': 48000, 'rating': 5, 'release_year': 2022},
        'Gigabyte X670E AORUS Master': {'brand': 'Gigabyte', 'model': 'X670E AORUS Master', 'socket': 'AM5', 'chipset': 'X670E', 'memory_type': 'DDR5', 'price': 46000, 'rating': 5, 'release_year': 2022},
        'MSI MEG X670E ACE': {'brand': 'MSI', 'model': 'MEG X670E ACE', 'socket': 'AM5', 'chipset': 'X670E', 'memory_type': 'DDR5', 'price': 52000, 'rating': 5, 'release_year': 2022},
    },
    'ssd': {
        'Samsung 990 Pro 2TB': {'brand': 'Samsung', 'model': '990 Pro', 'capacity': 2000, 'type': 'NVMe PCIe 4.0', 'read_speed': 7450, 'write_speed': 6900, 'price': 15000, 'rating': 5, 'release_year': 2022},
        'WD Black SN850X 2TB': {'brand': 'WD', 'model': 'Black SN850X', 'capacity': 2000, 'type': 'NVMe PCIe 4.0', 'read_speed': 7300, 'write_speed': 6600, 'price': 13000, 'rating': 5, 'release_year': 2022},
        'Crucial P5 Plus 2TB': {'brand': 'Crucial', 'model': 'P5 Plus', 'capacity': 2000, 'type': 'NVMe PCIe 4.0', 'read_speed': 6600, 'write_speed': 5000, 'price': 11000, 'rating': 4, 'release_year': 2021},
        'Samsung 980 Pro 1TB': {'brand': 'Samsung', 'model': '980 Pro', 'capacity': 1000, 'type': 'NVMe PCIe 4.0', 'read_speed': 7000, 'write_speed': 5000, 'price': 9000, 'rating': 5, 'release_year': 2020},
        'Kingston KC3000 2TB': {'brand': 'Kingston', 'model': 'KC3000', 'capacity': 2000, 'type': 'NVMe PCIe 4.0', 'read_speed': 7000, 'write_speed': 7000, 'price': 14000, 'rating': 5, 'release_year': 2021},
    }
}

@app.route('/')
def index():
    return render_template('index.html', components=components_data)

@app.route('/compare', methods=['POST'])
def compare():
    selected_components = []
    
    # Получаем выбранные компоненты из формы
    for category in components_data:
        selected = request.form.getlist(category)
        for item in selected:
            if item in components_data[category]:
                component = components_data[category][item].copy()
                component['type'] = category.upper()
                component['name'] = item
                selected_components.append(component)
    
    # Проверяем, что выбрано от 2 до 5 компонентов
    if len(selected_components) < 2:
        error = "Пожалуйста, выберите как минимум 2 компонента для сравнения."
        return render_template('index.html', components=components_data, error=error)
    elif len(selected_components) > 5:
        error = "Пожалуйста, выберите не более 5 компонентов для сравнения."
        return render_template('index.html', components=components_data, error=error)
    
    return render_template('results.html', components=selected_components)

if __name__ == '__main__':
    app.run(debug=True)