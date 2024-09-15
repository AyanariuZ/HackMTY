import React from 'react';
import { View, Text, StyleSheet, Image } from 'react-native';
  


const PromotionCard = ({description}) => {
  return (
    <View style={styles.cardContainer}>
      <Image
        source={{ uri: 'https://www.cityclub.com.mx/dw/image/v2/BGBD_PRD/on/demandware.static/-/Sites-soriana-grocery-master-catalog/default/dwb6931f7d/images/product/7501011101760.jpg?sw=1000&sh=1000&sm=fit' }} // Reemplaza con la URL de tu imagen
        style={styles.cardImage}
      />
      <View style={styles.cardContent}>
        <Text style={styles.cardTitle}>Nueva promoción</Text>
        <Text style={styles.cardDescription}>{description}</Text>
      </View>
    </View>
  );
};

const styles = StyleSheet.create({
  cardContainer: {
    width: '90%',
    backgroundColor: '#1e1e1e', 
    borderRadius: 10,
    overflow: 'hidden',
    elevation: 5,
    shadowColor: '#000', 
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.8,
    shadowRadius: 2,
    margin: 10,
  },
  cardImage: {
    width: '100%',
    height: 150,
  },
  cardContent: {
    padding: 15,
    backgroundColor: '#6a0dad',
  },
  cardTitle: {
    fontSize: 20,
    fontWeight: 'bold',
    color: '#fff',
    marginBottom: 5,
  },
  cardDescription: {
    fontSize: 16,
    color: '#ccc',
  },
});

export default PromotionCard;
