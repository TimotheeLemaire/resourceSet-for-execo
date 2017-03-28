import copy

#A Resource maps a computational resource to an object which keeps 
#Certains characteritics such as type, name, gateway.
class Resource():
	"""docstring for Resource"""
	# self.Type #type of the resource
	# self.properties #properties of the resources


    # Creates a new Resource Object.
    # self.param [type] type of the source
    # self.param [properties] object property
    # self.param [String] String name
	# self.return [resource] Resource Object
	def __init__(self,typ, prop=None , name = None):
		self.type = typ #type of the resource
		self.properties = dict()  #properties of the resources

		if prop: #test si prop est vide 
			#----replaces the contents of self.properties hash with
            #----contents of 'properties' hash
        	self.properties = prop  

		if name :
			self.properties["name"] = name 

 #     __getattribute__(...)
 # |      x.__getattribute__('name') <==> x.name

	# Return the name of the resource.
	# self.return [String] the name of the resource
    def name(self) :
        return self.properties["name"]
    

	#Sets the name of the resource.
    def name_equal(self,name):
        self.properties["name"] = name
        return self
    

    def ssh_user(self):
        return self.properties["ssh_user"]
    
    
    def gw_ssh_user(self):
    	return self.properties["gw_ssh_user"]
    
	#Returns the name of the resource.
    def to_s(self):	
        return self.properties["name"]
    

    def corresponds(self, props ):
        for key,value in props:
            if callable(value) :
                if not value(self.properties[key]):
                    return False
            else :
                if (self.properties[key] != value):
                    return False
        return True

    
  
    #Creates a copy of the resource object.
    def copy(self):
        result = Resource(self.type)
        result.properties =  self.properties 
        return result
    

    #Equality, Two Resource objects are equal if they have the 
    #same type and the same properties as well.
    def __eq__( self,res ): 
        return self.type == res.type and self.properties == res.properties
    

    #Returns true if self and other are the same object.
    def eql( self,res ):
        if self.type == res.type and self.__class__ == res.__class__:
            for key,value in self.properties:
                if(res.properties[key] != value):
                    return False 
            return True 
        else :
            return False

	#Returns the name of the gateway
	def gateway(self):
		if self.properties["gateway"]:
            return self.properties["gateway"] 
		return "localhost"
	

    def gateway_equal(self,host):
      self.properties["gateway"] = host
      #return self
    
    	
	#alias gw gateway

    def job(self):
        if self.properties["id"]:
            return self.properties["id"] 
      return 0




"""TODO"""
#Use to make the list of machines for
#the taktuk command
    def make_taktuk_command(cmd):
            return " -m #{self.name}"
    



#class ResourceSetIterator

"""********************************
classe resourceSet  : 
    

***********************************"""
class ResourceSet < Resource
        #attr_accessor :resources
        
        def __init__(self, name = None ):
                super( self.resource_set, None, name )
                self.resources = []
                self.resource_files = dict()
        

    #Creates a copy of the ResourceSet Object
        def copy(self):
                result = ResourceSet()
                result.properties = self.properties 
                for resource in self.resources :
                    result.resources.append(copy.deepcopy(ressource))

                return result
        

    #Add a Resource object to the ResourceSet
    #//on devrait peut être le renommer en append ? 
        def append(self, resource ):
          self.resources.append( resource )
          return self
        

    # Return the first element which is an object of the Resource Class
        def first (self, type=None ):
            for resource in self.resources:
                if (resource.type == type) :
                    return resource
                elif types(resource) == ResourceSet :
                    res = resource.first( type )
                    if (res) :
                        return res 
                elif (not type) :
                    return resource
            return None
        

        def select_resource(self, props ):
            for resource in self.resources:
                if resource.corresponds( props ) :
                    return resource


        def select(self, type=None, props=None , block=None):
            set = ResourceSet()
            if not block :
                set.properties = self.properties 
                for resource in resources :
                    if not type or resource.type == type :
                        if resource.corresponds( props ) :
                            set.resources.append( resource.copy )
                                
                        elif type != :resource_set and resource,ResourceSet) :
                                set.resources.append( resource.select( type, props ) )
                
            else :
                set.properties = self.properties 
                for resource in resources :
                    if not type or resource.type == type :
                        if block( resource ) :
                            set.resources.append( resource.copy )
                            
                    elif type != resource_set and isinstance(resource,ResourceSet) :
                            set.resources.append( resource.select( type, props , block) )
            return set
    

        def delete_first(self,resource):
            for i in range(len(self.resources)) :
                if self.resources[i] == resource :
                    self.resources.pop(i)
                    return resource
                elif isistance(self.resources[i],ResourceSet) :
                    if self.resources[i].delete_first( resource ) :
                        return resource
            return None
        

        def delete_first_if(self,block=None):
                for i in range(len(self.resources)) :
                    if block(self.resources[i]) :
                        return self.resources.pop(i)
                    elif isistance(self.resources[i],ResourceSet) :
                        if (res = self.resources[i].delete_first_if( block )) :
                            return res
                return None
        
        #del ? __del__
        def delete(self,resource):
                res = None
                for i in range(len(self.resources)) :
                    if self.resources[i] == resource :
                        self.resources.pop(i)
                        res = resource
                    elif isinstance(self.resources[i],ResourceSet) :
                        #if self.resources[i].delete_all( resource ) :
                        if self.resources[i].delete( resource ) :
                            res = resource
                return res
        

        def delete_if(self,block=None):
            for i in range(len(self.resources)) :
                if block(self.resources[i]) :
                    self.resources.pop(i)
                elif isinstance(self.resources[i],ResourceSet) :
                    self.resources[i].delete_if( block )
            return self
        

    #Puts all the resource hierarchy into one ResourceSet.
    #The type can be either :node or :resource_set.
        def flatten(self, type = None ):
            set = ResourceSet()
            for resource in self.resources:
                if not type or resource.type == type :
                    set.resources.append( resource.copy )
                    if isinstance(resource,ResourceSet) :
                        del set.resources[-1].resources[:]
                if isinstance(resource,ResourceSet) :
                    set.resources.extend( resource.flatten(type).resources )
            return set
        

        # def flatten! (self,type = None ):
        def flatten_not (self,type = None ):
            set = self.flatten(type)
            self.resources = set.resources 
            return self
        


        # alias all flatten

    #Creates groups of increasing size based on
    #the slice_step paramater. This goes until the 
    #size of the ResourceSet.
    def each_slice( self,type = None, slice_step = 1, block=None):
        i = 1
        number = 0
        while True :
            resource_set = ResourceSet()
            it = ResourceSetIterator(self, type)
            #----is slice_step a block? if we call from
            #----each_slice_power2 : yes
            
            #if isinstance(slice_step,Proc) :
            if callable(slice_step):
                number = slice_step(i)

            elif isinstance(slice_step,list) :
                number = slice_step.shift.to_i
                else :
                    number += slice_step
            return None if number == 0
            for j in 1..number do
                    resource = it.resource
                    if resource :
                            resource_set.resources.append( resource )
                    else :
                        return None
                    
                    it.next
            
            block( resource_set );
            i += 1
                 
        

    #Invokes the block for each set of power of two resources.
        def each_slice_power2(self, type = None, block=None ):
            self.each_slice( type, lambda i :  i*i , block )
        

    def each_slice_double( self,type = None, block=None ):
        self.each_slice( type, lambda i :  2**i , block )
    
        ## Fix Me  is the type really important , or were are going to deal always with nodes
        def each_slice_array( self,slices=1, block=None):
          self.each_slice( None,slices, block)
        

    #Calls block once for each element in self, depending on the type of resource.
    #if the type is :resource_set, it is going to iterate over the several resoruce sets defined.
    #:node it is the default type which iterates over all the resources defined in the resource set.
    def each( self,type = None, block=None ):
        it = ResourceSetIterator(self, type)
        while it.resource() :
            block( it.resource() )
            it.next()
                
        
    """TODO !!! """
    # Returns the number of resources in the ResourceSet
    # self.return [Integer] the number of resources
    """
    def length(self):
        count=0
        self.each("node",lambda count : count+=1) # impossible d'incrémenter en fonction lambda
        return count
"""
 # |      x.__getattribute__('name') <==> x.name
        #__getattribute('resource')
    def lentgth(self):
        count = 0 
        it = ResourceSetIterator(self, "node")
        while it.resource() :
            #block( it.resource )
            count += 1
            it.next()
        return count
    

    # Returns a subset of the ResourceSet.
    # self.note It can be used with a range as a parameter.
        # self.param [Range] index  Returns a subset specified by the range.
        # self.param [String] index Returns a subset which is belongs to the same cluster.
        # self.param [Integer] index    Returns just one resource.
    # self.return [ResourceSet]     a ResourceSet object
    # self.example 
    #   all[1..6] extract resources from 1 to 6
    #   all["lyon"] extract the resources form lyon cluster
    #   all[0]  return just one resource.
    def __getitem__( self,index ):
        count=0
        resource_set = ResourceSet::new
        it = ResourceSetIterator::new(self,:node)
        if isinstance(index,list) :
                self.each(:node){ |node|
            resource=it.resource
            if resource :
                if (count >= index.first ) and (count <= index.max) :
                                        resource_set.resources.push( resource )
                                
                        
                        count+=1
                        it.next
                }
        resource_set.properties=self.properties.clone
                return resource_set
      
          if index.kind_of?(String) :
          it = ResourceSetIterator::new(self,:resource_set)
            self.each(:resource_set) { |resource_set|
                  if resource_set.properties[:alias] == index :
                    return resource_set
                  
            }
         
          #For this case a number is passed and we return a resource Object
              self.each(:node){ |resource|
           resource=it.resource
               if resource :
                    if count==index :
               #resource_set.resources.push( resource )
                           return resource
                    
           
                   count+=1
           it.next
              }
        
    

    # Returns a resouce or an array of resources.
    # self.return [Resource] a resource or array of resources
    def to_resource(self)  :
        if self.length() == 1 :
            


            self.each("node"){ |resource|
                return resource
            }
        else :
            resource_alist= [] 
            self.each("node"){ 
                resource_array.append( resource )
                }
            return resource_array
        
    

        def __eq__( set ):
                super and self.resources == set.resources
        

    #Equality between to resoruce sets.
        def eql( set ) :
                super and self.resources == set.resources
        

    # Returns a ResourceSet with unique elements.
    # self.return [ResourceSet]     with unique elements
        def uniq():
                set = self.copy
                return set.uniq!
        

        def uniq!
          i = 0
          while i < self.resources.size-1 do
            pos = []
              for j in i+1...self.resources.size
                                      if self.resources[i].eql?(self.resources[j]) :
                pos.append(j)
                                      
                              
            pos.reverse.each { |p|
                                      self.resources.delete_at(p)
            }
            i = i + 1 
                      
                      self.resources.each { |x|
                              if x.instance_of?(ResourceSet) :
                                      x.uniq!
                              
                      }
                      return self
        

    # Generates and return the path of the file which contains the list of the tipe of resource
    #specify by the argument type.
        def resource_file( type=None, update=false )
            if ( not self.resource_files[type] ) or update :
                    self.resource_files[type] = Tempfile("#{type}")
                    resource_set = self.flatten(type)
                    resource_set.each { |resource|
                            self.resource_files[type].puts( resource.properties[:name] )
                    }
                    self.resource_files[type].close
                    File.chmod(0644, self.resource_files[type].path)
            
            return self.resource_files[type].path
        

    #Generates and return the path of the file which contains the list  of the nodes' hostnames. Sometimes it is handy to have it.
    #eg. Use it with mpi.    
    def node_file( update=false ):
            resource_file( "node", update )
        

    #alias nodefile node_file

    def gen_keys(type=None )
        puts "Creating public keys for cluster ssh comunication"
        resource_set = self.uniq.flatten(type)
        resource_set.each { |resource|
            cmd = "scp "
            cmd += "-r ~/.ssh/ "
            ### here we have to deal with the user ## we have to define one way to put the user.
            cmd += " rootself.#{resource.properties[:name]}:~"
            command_result = $client.asynchronous_command(cmd)
            $client.command_wait(command_result["command_number"],1)
            result = $client.command_result(command_result["command_number"])
            puts cmd
            puts result["stdout"]
            puts result["stderr"]
        }
    
    #Generates a directory.xml file for using as a resources 
    #For Gush.
    def make_gush_file( update = false)
        gush_file = File("directory.xml","w+")
        gush_file.puts("<?xml version=\"1.0\" encoding=\"UTF-8\"?>")
        gush_file.puts("<gush>")
        resource_set = self.flatten(:node)
        resource_set.each{ |resource|
            gush_file.puts( "<resource_manager type=\"ssh\">")
            gush_file.puts("<node hostname=\"#{resource.properties[:name]}:15400\" user=\"lig_expe\" group=\"local\" />" )

            gush_file.puts("</resource_manager>")
        }
        gush_file.puts("</gush>")
        gush_file.close
        return gush_file.path
    

    #Creates the taktuk command to execute on the ResourceSet
    #It takes into account if the resources are grouped under
    #different gatways in order to perform this execution more
        #efficiently.
        def make_taktuk_command(self)
                str_cmd = ""
                #pd : séparation resource set/noeuds
                if self.gw != "localhost" :
                        sets = false
                  sets_cmd = ""
                        self.resources.each { |x|
                                if x.instance_of?(ResourceSet) :
                                        sets = true
                                        sets_cmd += x.make_taktuk_command(cmd)
                                
                        }
                        str_cmd += " -m #{self.gw} -[ " + sets_cmd + " -]" if sets
                        nodes = false
                        nodes_cmd = ""
                        self.resources.each { |x|
                                if x.type == :node :
                                        nodes = true
                                        nodes_cmd += x.make_taktuk_command(cmd)
                                
                        }
                  str_cmd += " -l #{self.gw_ssh_user} -m #{self.gw} -[ -l #{self.ssh_user} " + nodes_cmd + " downcast exec [ #{cmd} ] -]" if nodes
                else :
                        nodes = false
                        nodes_cmd = ""
                        first = ""
                        self.resources.each { |x|
                                if x.type == :node :
                                        first = x.name if not nodes
                                        nodes = true
                                        nodes_cmd += x.make_taktuk_command(cmd)
                                
                        }
                  puts " results of the command #{nodes_cmd}"
                  str_cmd += " -l #{self.gw_ssh_user} -m #{first} -[ " + nodes_cmd + " downcast exec [ #{cmd} ] -]" if nodes
                        sets = false
                        sets_cmd = ""
                        self.resources.each { |x|
                                if x.instance_of?(ResourceSet) :
                                        sets = true
                                        sets_cmd += x.make_taktuk_command(cmd)
                                
                        }
                        if sets :
                                if nodes : 
                                        str_cmd += " -m #{first} -[ " + sets_cmd + " -]"
                                else
                                        str_cmd += sets_cmd
                                
                        
                
                return str_cmd
        



class ResourceSetIterator:
        #current : élement courant 
        #iterator : resource set pour parcourir les resource_set 
        #resource_set: la resource initale 
        #type : le type de la resource initiale
        #
        #
        #attr_accessor :current, :iterator, :resource_set, :type
        def initialize(self, resource_set, type=None)
                self.resource_set = resource_set
                self.iterator = None
                self.type = type
                self.current = 0
               
                for i in range(len(resource_set.resources)) :
                    if self.type == self.resource_set.resources[i].type :
                                self.current = i
                                return 
                    elif isinstance(self.resource_set.resources[i],ResourceSet) :
                        self.iterator = ResourceSetIterator(self.resource_set.resources[i], self.type)
                        if self.iterator.resource :
                            self.current = i
                            return
                        else
                            self.iterator = None
                                
                    elif not self.type :
                        self.current = i
                        return
                self.current = self.resource_set.resources.size
        
 #         __getattribute__(...)
 # |      x.__getattribute__('name') <==> x.name
        #__getattribute('resource')
        #
        #
        def resouce(self):
                if( self.current >= self.resource_set.resources.size ):
                    return None 
                if self.iterator :
                    res = self.iterator.resource()

                else :
                    res = self.resource_set.resources[self.current]
                
                return res
        

        def next(self):
            res = None
            self.current += 1 if not self.iterator
            while not res and self.current < self.resource_set.resources.size : 
                    if self.iterator :
                            self.iterator.next
                            res = self.iterator.resource
                            if not res :
                                    self.iterator = None
                                    self.current += 1
                            
                    elif self.type == self.resource_set.resources[self.current].type :
                            res = self.resource_set.resources[self.current]
                    elif isinstance(self.resource_set.resources[self.current],ResourceSet) :
                            self.iterator = ResourceSetIterator(self.resource_set.resources[self.current], self.type)
                            res = self.iterator.resource()
                            if not res :
                                    self.iterator = None
                                    self.current += 1
                            
                    elif not self.type :
                            res = self.resource_set.resources[self.current]
                    else
                            self.current += 1
                    
            if( self.current >= self.resource_set.resources.size ) :
                raise StopIteration
                self.current = 0
                return None 
            if self.iterator :
                res = self.iterator.resource()

            else :
                res = self.resource_set.resources[self.current]
            
            return res
        
        def __iter__(self):
            return self





