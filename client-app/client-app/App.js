import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View, ScrollView } from 'react-native';
import PromotionCard from './Components/PromotionCard';

promotionList = {
  "promotionList": [
    {
      "description": "Hay un 2 x 1 en refrescos"
    },
    {
      "description": "Descuento del 20% en todos los snacks"
    },
    {
      "description": "Compra un café y recibe una dona gratis"
    },
    {
      "description": "Descuento del 15% en compras superiores a $500"
    },
    {
      "description": "3x2 en productos de limpieza seleccionados"
    }
  ]
}


export default function App() {
  return (
    <View style={styles.container}>
      <ScrollView contentContainerStyle={styles.scrollViewContainer}>
        {promotionList.promotionList.map((promotion, index) => (
          <PromotionCard key={index} description={promotion.description} />
        ))}
      </ScrollView>
      <StatusBar style="auto" />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    marginTop: '10%',
    flex: 1,
    backgroundColor: '#fff',
  },
  scrollViewContainer: {
    alignItems: 'center',
    paddingVertical: 20,
  },
});