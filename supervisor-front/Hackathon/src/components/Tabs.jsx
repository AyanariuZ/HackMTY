import {Tabs, Tab} from "@nextui-org/react";

export default function TabsComponent({children}) {
  return (
    <div className="flex w-full flex-col items-center">
        
        <Tabs aria-label="Options">
      <Tab key="all" title="Todas" className="flex flex-wrap justify-start">
      <div className="flex flex-row flex-wrap justify-center">
        {children}
        </div>  
        </Tab>
        <Tab key="2x1" title="2x1" className="flex flex-wrap justify-start">
        <div className="flex flex-row flex-wrap justify-center">
        {children.filter(child => child.props.discountType === "2x1")}
        </div> 
        </Tab>
        <Tab key="Fijo" title="Fijo" className="flex flex-wrap justify-start">
        <div className="flex flex-row flex-wrap justify-center">
        {children.filter(child => child.props.discountType === "Fijo")}
        </div>
        </Tab>
        <Tab key="Combo" title="Combo " className="flex flex-wrap justify-start ">
        <div className="flex flex-row flex-wrap justify-center">
        {children.filter(child => child.props.discountType === "Combo")}
        </div>
        </Tab>
      </Tabs>
        </div>
      
    
  );
}