import { Card, CardFooter, Image} from "@nextui-org/react";
import {Modal, ModalContent, ModalHeader, ModalBody, ModalFooter, Button, useDisclosure} from "@nextui-org/react";
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faTrash } from '@fortawesome/free-solid-svg-icons'
import { faCheck } from '@fortawesome/free-solid-svg-icons'

export default function RecoCard({title, discountType, image, discountLabel}) {
  const { isOpen, onOpen, onOpenChange } = useDisclosure();

  return (
    <>
      <Card
        isFooterBlurred
        radius="lg"
        className="border-none w-auto items-center relative cursor-pointer dark m-4"
        isPressable
        onPress={onOpen}
      >
        <Image
          alt="Woman listening to music"
          className="object-cover"
          height={200}
          src="https://nextui.org/images/hero-card.jpeg"
          width={200}
        />
        <CardFooter className="before:bg-white/10 border-white/20 border-1 overflow-hidden py-1 absolute before:rounded-xl rounded-large bottom-1 shadow-small z-10 w-auto flex justify-center items-center pt-0">
          {discountLabel}
        </CardFooter>
      </Card>
      <Modal isOpen={isOpen} onOpenChange={onOpenChange} placement='center' backdrop='blur' className='dark text-white'>
        <ModalContent>
          {(onClose) => (
            <>
              <ModalHeader className="flex flex-col gap-1 text-center">{discountLabel}</ModalHeader>
              <ModalBody className='gap-0'>
              <Image
              alt="Imagen de la oferta"
              src="https://nextui.org/images/hero-card.jpeg"
              width={100}
              height={100}
              className="rounded-lg absolute top-0 left-0"
            />
                <p className='pl-28 top-0 text-justify'> 
                  Lorem ipsum dolor sit amet, consectetur adipiscing elit.
                  Nullam pulvinar risus non risus hendrerit venenatis.
                  
                </p>
                <div className="flex flex-wrap gap-2 m-6 justify-center bottom-0.5 mb-0">
                <span className="bg-primary/20 text-primary text-xs font-medium px-2.5 py-0.5 rounded">Exclusivo</span>
                <span className="bg-success/20 text-success text-xs font-medium px-2.5 py-0.5 rounded">Tiempo limitado</span>
                <span className="bg-warning/20 text-warning text-xs font-medium px-2.5 py-0.5 rounded">{discountType}</span>
              </div>
              </ModalBody>
              <ModalFooter className='justify-center'>
                
                <Button color="danger" onPress={onClose} className='rounded-full w-10 h-10 min-w-0'>
                <FontAwesomeIcon icon={faTrash} />
                </Button>
                <Button color="success" onPress={onClose} className='rounded-full w-10 h-10 min-w-0'>
                <FontAwesomeIcon icon={faCheck} inverse/>
                </Button>
            </ModalFooter>
            </>
          )}
        </ModalContent>
      </Modal>
    </>
  );
}