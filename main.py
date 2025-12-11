from core import utils
from core import output_string

if __name__ == '__main__':
    ip_input = utils.get_ip()
    subnet_mask = utils.get_mask()
    cidr = utils.to_CIDR(subnet_mask)
    ip_list = utils.to_list_ip(ip_input)
    result = utils.make_ip_to_network(cidr, ip=ip_list) # dict
    result['subnet_mask'] = subnet_mask 
    result['type_class'] = utils.check_classless_or_classful(cidr)
    utils.seve_data(output_string.format_input_ip(ip_input))
    utils.seve_data(output_string.format_subnet_mask(subnet_mask))
    utils.seve_data(output_string.format_classful_status(result['type_class']))
    utils.seve_data(output_string.format_network_address(result['Network']))
    utils.seve_data(output_string.format_broadcast_address(result['brodcast']))
    utils.seve_data(output_string.format_num_hosts(result['possible_host']))
    utils.seve_data(output_string.format_cidr_mask(cidr))