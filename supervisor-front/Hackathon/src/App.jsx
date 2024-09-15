import './App.css'
import { Cameras } from './components/cameras'
import Navbar from './components/Navbar'
import Carousel from './components/Carousel'
import RecoCard from './components/RecoCard'
import Tabs from './components/Tabs'
function App() {
  const data = [
    {
      discountType: "2x1",
      image: "https://nextui.org/images/hero-card.jpeg",
      discountLabel: "2x1 en bebidas"
    },
    {
      discountType: "Fijo",
      image: "https://nextui.org/images/hero-card.jpeg",
      discountLabel: "30% de descuento en ropa"
    },
    {
      discountType: "Combo",
      image: "https://nextui.org/images/hero-card.jpeg",
      discountLabel: "Llévate un combo de hamburguesa"
    },
    {
      discountType: "2x1",
      image: "https://nextui.org/images/hero-card.jpeg",
      discountLabel: "2x1 en entradas de cine"
    },
    {
      discountType: "Fijo",
      image: "https://nextui.org/images/hero-card.jpeg",
      discountLabel: "20% de descuento en zapatos"
    },
    {
      discountType: "Combo",
      image: "https://nextui.org/images/hero-card.jpeg",
      discountLabel: "Combo de 2 pizzas por el precio de 1"
    },
    {
      discountType: "2x1",
      image: "https://nextui.org/images/hero-card.jpeg",
      discountLabel: "2x1 en snacks"
    },
    {
      discountType: "Fijo",
      image: "https://nextui.org/images/hero-card.jpeg",
      discountLabel: "50% de descuento en gafas de sol"
    },
    {
      discountType: "Combo",
      image: "https://nextui.org/images/hero-card.jpeg",
      discountLabel: "Combo de desayuno + café"
    },
    {
      discountType: "2x1",
      image: "https://nextui.org/images/hero-card.jpeg",
      discountLabel: "2x1 en postres"
    },
    {
      discountType: "Fijo",
      image: "https://nextui.org/images/hero-card.jpeg",
      discountLabel: "15% de descuento en electrónicos"
    },
    {
      discountType: "Combo",
      image: "https://nextui.org/images/hero-card.jpeg",
      discountLabel: "Combo de cine: palomitas + refresco"
    }
  ];
  


  return (
    <>

    
    <Cameras >
    <div className='backdrop-blur-md h-screen'>
      <Navbar>
    </Navbar>
    <Carousel>
    {data.map((item, index) => (
        <RecoCard
          key={index}
          discountType={item.discountType}
          image={item.image}
          discountLabel={item.discountLabel}
        />
      ))}
    </Carousel>
    <Tabs>
    {data.map((item, index) => (
        <RecoCard
          key={index}
          discountType={item.discountType}
          image={item.image}
          discountLabel={item.discountLabel}
        />
      ))}
    </Tabs>
    </div>
    
    </Cameras>
    
    </>
  )
}

export default App
